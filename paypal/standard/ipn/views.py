#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Generic Stuff
from django.http import HttpResponse, QueryDict, Http404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse 
from django.shortcuts import render, get_object_or_404, render_to_response
from django.conf import settings
from urllib import quote
#Import Paypal and IPN forms, modesl
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.ipn.forms import PayPalIPNForm
from paypal.standard.ipn.models import PayPalIPN
#Scheduling Stuff
import datetime
from datetime import timedelta
import pytz
from django.utils import timezone
#Import CORE models
from core.models import UserInfo
from connections.models import Connection
#import transaction models
from transactions.models import Transaction
from transactions.forms import CreatePackageTransaction
from transactions.views import notify_host_shipment_paid, notify_enduser_shipment_paid
##Adding email functionality (http://catherinetenajeros.blogspot.com/2013/03/send-mail.html)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.list import ListView


@require_POST
@csrf_exempt
def ipn(request, item_check_callable=None, host_id=None, trans_id=None):
    """
    PayPal IPN endpoint (notify_url).
    Used by both PayPal Payments Pro and Payments Standard to confirm transactions.
    http://tinyurl.com/d9vu9d
    
    PayPal IPN Simulator:
    https://developer.paypal.com/cgi-bin/devscr?cmd=_ipn-link-session
    
    #what triggers this view?
    """
    #TODO: Clean up code so that we don't need to set None here and have a lot
    #      of if checks just to determine if flag is set.
    flag = None
    ipn_obj = None
    
    # Clean up the data as PayPal sends some weird values such as "N/A"
    # Also, need to cope with custom encoding, which is stored in the body (!).
    # Assuming the tolerant parsing of QueryDict and an ASCII-like encoding,
    # such as windows-1252, latin1 or UTF8, the following will work:

    encoding = request.POST.get('charset', None)

    if encoding is None:
        flag = "Invalid form - no charset passed, can't decode"
        data = None
    else:
        try:
            data = QueryDict(request.body, encoding=encoding).copy()
        except LookupError:
            data = None
            flag = "Invalid form - invalid charset"

    if data is not None:
        date_fields = ('time_created', 'payment_date', 'next_payment_date',
                       'subscr_date', 'subscr_effective')
        for date_field in date_fields:
            if data.get(date_field) == 'N/A':
                del data[date_field]

        form = PayPalIPNForm(data) #from paypal.standard.ipn.forms import PayPalIPNForm
        if form.is_valid():
            try:
                #When commit = False, object is returned without saving to DB.
                ipn_obj = form.save(commit=False)
            except Exception as e:
                flag = "Exception while processing. (%s)" % e
        else:
            flag = "Invalid form. (%s)" % form.errors
		    
    if ipn_obj is None:
        ipn_obj = PayPalIPN() #from paypal.standard.ipn.models import PayPalIPN
        
    #Set query params and sender's IP address
    ipn_obj.initialize(request)
    
    #Store the invoice value so i can use it to update the transactions model
    invoice_sent = ipn_obj.invoice
    
    #Add other host characteristicsto the model
    #Eventually add transaction_id to the ipn_obj model
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
        ipn_obj.host_email = host.email
        ipn_obj.host_fname = host.first_name
        ipn_obj.host_lname = host.last_name
        ipn_obj.host_st_address1 = host.st_address1
        ipn_obj.host_st_address2 = host.st_address2
    if trans_id:
        trans = Transaction.objects.get(pk=trans_id) 
        ipn_obj.trans_table_id = trans.id	
    #the following set_flag is defined in paypal.standard.modle.spy, flat var is passed as the "info" parameter
    if flag is not None:
        #We save errors in the flag field
        ipn_obj.set_flag(flag)
    else:
        # Secrets should only be used over SSL.
        if request.is_secure() and 'secret' in request.GET:
            ipn_obj.verify_secret(form, request.GET['secret'])
        else:
            ipn_obj.verify(item_check_callable)

    ipn_obj.save()
    ipn_obj.send_signals()
    
    #JMY ADDED: Update the Transaction Table to confirm we need to transation ID but only have invoice on the paypal IPN
    if trans_id:
        trans.payment_processed = True
        trans_table_id = trans.id
        trans.payment_method = "Paypal"
        trans.save()
        #update the userinfo table to add an account balance
        new_balance = trans.balance_created_packages
        userinfo = UserInfo.objects.get(pk=trans.enduser.id)
        if new_balance:
    		    userinfo.account_balance_packages = new_balance
    		    userinfo.save()
        #send emails
        notify_host_shipment_paid(request,trans_table_id)
        notify_enduser_shipment_paid(request, trans_table_id) 
    return HttpResponse("OKAY")

#The paypal_ipn view: www.blocbox.co/transactions/ipn: Instant Payment Notification
"""About the IPN: After completing the purchase PayPal makes an HTTP
POST to your `notify_url`. PayPal calls this process [Instant Payment
Notification](https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_OrderMgmt_IntegrationGuide.pdf)
(IPN) but you may know it as [webhooks](http://www.webhooks.org/). This method
kinda sucks because it drops your customers off at PayPal's website but it's
easy to implement and doesn't require SSL."""

""" the ask for money view is triggered in the shipment process after they've confirmed availability
		the page first display a form asking for the payment option (bundled, per package, etc) and gets 
		a label for the transaction (title) and a note to the host (note_to_host)
		once that form has been submitted, a new page is rendered that asks them to confirm infomration
		and link to their paypal accout.
		the template for both of these is on payment.html
"""
def ask_for_money(request, host_id=2, favortype=None, invoice=None,): #pass teh favor type and invoice in the URL pattern (www.blocbox.co/transactions/payment/
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    #Define the business/receiver email (frsturated b/c the business name is the receiver email name, can't decouple)
    if host.email:
        business = host.email
    else:
        business = settings.PAYPAL_RECEIVER_EMAIL #want it to show as business name (Blocbox)
    returnmessage = "Return to Blocbox and Ship Your Package to " + host.first_name     
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    #Update transaction table
    datenow = datetime.datetime.now()  
    date = datetime.date.today()
    time = datetime.datetime.time(datenow)
    paypal_quantity = 1  
    #NEXT, add the paypal fields
    #For a list of fields: https://developer.paypal.com/webapps/developer/docs/classic/paypal-payments-standard/integration-guide/Appx_websitestandard_htmlvariables/
    #THEN.. after transaction entry created - retrive the info - including transaction ID 
    #Get the transactions record that was just created
    trans_created = Transaction.objects.get(invoice=invoice)
    #Account balance
    if enduser.account_balance_packages:
        if enduser.account_balance > 0:
            remaining_balance = enduser.account_balance_packages - 1
        else:
            remaining_balance = 0
    else:
        remaining_balance = None
    paypal_dict = {
        "business": business, #settings.PAYPAL_RECEIVER_EMAIL,  #THIS is causing it to show as 'return to admin@blocbox.co'
        "amount": trans_created.amount_due, #Amount of the purchase - try to pass this as an argument
        "item_name": favortype,
        "quantity": paypal_quantity,
        "cbt": returnmessage, #Sets value for return to merchant button
        "image_url": "http://www.blocbox.co/static/blocbox/images/Logo-and-name---orange-drop2_paypal.png",
        "invoice": invoice,
        #Need to add a filed fo rhost_emai, figuore out how to flag "payment sent"
        #Receiver email:  	Primary email address of the payment recipient (that is, the merchant). 
        #If the payment is sent to a non-primary email address on your PayPal account, the receiver_email is still your primary email. 
        "custom": enduser.email, #this is serving as the User Email field
        "notify_url": "http://www.blocbox.co/transactions/ipn/notify" + str(host.id) +"/" + str(trans_created.id) + "/",
        "return_url": "http://www.blocbox.co/transactions/shippackage/host" + str(host.id) +"/",
        "cancel_return": "http://www.blocbox.co/dashboard/",
    }   
    paypal_form = PayPalPaymentsForm(initial=paypal_dict) #in paypal/standard/forms.py
    #context = {"for: form}
    return render(request, 'blocbox/payment_enter_paypal.html', {
		    'enduser':enduser, 'host':host, 'invoice': invoice, 'remaining_balance': remaining_balance,
    	  'date':datenow, 'local_timezone':local_timezone, 
    	  'here': quote(request.get_full_path()), 'paypal_form': paypal_form, 'trans_created': trans_created, 'invoice': invoice,     	  
    })




    
"""Need to implement a return view and a cancel view, from documentation:
 	You will also need to implement the 'return_url' and 'cancel_return' views
   to handle someone returning from PayPal. Note that these views need
   @csrf_exempt applied to them, because PayPal will POST to them, so they
   should be custom views that don't need to handle POSTs otherwise.

   For 'return_url' you need to cope with the possibility that the IPN has not
   yet been received and handled by the IPN listener you implemented (which can
   happen rarely), or that there was some kind of error with the IPN.
 

EXAMPLE FROM WEBSITE: https://github.com/chrisglass/django-shop-paypal/blob/master/shop_paypal/offsite_paypal.py
@csrf_exempt
def paypal_successful_return_view(self, request):
    if getattr(settings, "PAYPAL_SUCCESS_REDIRECT_TO_THANKYOU", False):
        return HttpResponseRedirect(self.shop.get_finished_url())
    rc = RequestContext(request, {})
    return render_to_response("shop_paypal/success.html", rc)

"""

#Return view - HOW DO I MAKE IT FILL IN JOHN INFO??
@csrf_exempt
def ipn_return_successful(request): #May need a "self" argumetn here
		#return render(request, 'blocbox/shippackage.html')
		return HttpResponseRedirect(reverse('shippackage'))
    #return HttpResponseRedirect(reverse('dashboard'))

