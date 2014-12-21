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


@require_POST
@csrf_exempt
def ipn(request, item_check_callable=None, host_id=None):
    """
    PayPal IPN endpoint (notify_url).
    Used by both PayPal Payments Pro and Payments Standard to confirm transactions.
    http://tinyurl.com/d9vu9d
    
    PayPal IPN Simulator:
    https://developer.paypal.com/cgi-bin/devscr?cmd=_ipn-link-session
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
    
    #Add other host characteristicsto the model
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
        ipn_obj.host_email = host.email
        ipn_obj.host_fname = host.first_name
        ipn_obj.host_lname = host.last_name
        ipn_obj.host_st_address1 = host.st_address1
        ipn_obj.host_st_address2 = host.st_address2
    
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
    return HttpResponse("OKAY")

#The paypal_ipn view: www.blocbox.co/payment/ipn: Instant Payment Notification
"""About the IPN: After completing the purchase PayPal makes an HTTP
POST to your `notify_url`. PayPal calls this process [Instant Payment
Notification](https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_OrderMgmt_IntegrationGuide.pdf)
(IPN) but you may know it as [webhooks](http://www.webhooks.org/). This method
kinda sucks because it drops your customers off at PayPal's website but it's
easy to implement and doesn't require SSL."""
def ask_for_money(request, host_id=2, favortype="package", paymentoption="perpackage", dayrangestart=None, dayrangeend=None): #default amount is 2.00, default host is John
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    if paymentoption=="bundle10":
        amount="15.00"
        youselected="Bundle of 10 Packages"
        quantity = 1
        quantity = 10
    elif paymentoption=="month20":
        amount="15.00"
        youselected="Monthly"
        quantity = 20
    elif paymentoption=="annual":
        amount="150.00"
        youselected="Annual"
        quantity = 240
    else:
        amount="2.00"
        youselected="Per Package"
        quantity = 1
    #Define the business/receiver email (frsturated b/c the business name is the receiver email name, can't decouple)
    if host.email:
        business = host.email
    else:
        business = settings.PAYPAL_RECEIVER_EMAIL #want it to show as business name (Blocbox)
    returnmessage = "Return to Blocbox and Ship Your Package to " + host.first_name
    transcount = PayPalIPN.objects.filter(receiver_email=host.email).count() + 1 #counts transactions that this receiver_email has received (could change to host email) 
    date = datetime.datetime.now()
    time = datetime.datetime.time(date)
    invoice = "h" + str(host.id) + "u" + str(enduser.id) + "n" +str(transcount) +"d" + str(date.month) + str(date.day) + str(time.hour) #h2u14n13d112210 = transaciton between host2, user14, host's 13th transaction
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    #For a list of fields: https://developer.paypal.com/webapps/developer/docs/classic/paypal-payments-standard/integration-guide/Appx_websitestandard_htmlvariables/
    paypal_dict = {
        "business": business, #settings.PAYPAL_RECEIVER_EMAIL,  #THIS is causing it to show as 'return to admin@blocbox.co'
        "amount": amount, #Amount of the purchase - try to pass this as an argument
        "item_name": favortype,
        "quantity": quantity,
        "cbt": returnmessage, #Sets value for return to merchant button
        "image_url": "http://www.blocbox.co/static/blocbox/images/Logo-and-name---orange-drop2_paypal.png",
        "invoice": invoice,
        #Need to add a filed fo rhost_emai, figuore out how to flag "payment sent"
        #Receiver email:  	Primary email address of the payment recipient (that is, the merchant). 
        #If the payment is sent to a non-primary email address on your PayPal account, the receiver_email is still your primary email. 
        "custom": enduser.email, #this is serving as the User Email field
        "notify_url": "http://www.blocbox.co/payment/ipn/notify" + str(host.id) +"/",
        "return_url": "http://www.blocbox.co/shippackage/host" + str(host.id) +"/",
        "cancel_return": "http://www.blocbox.co/dashboard/",
    }    
    form = PayPalPaymentsForm(initial=paypal_dict) #in paypal/standard/forms.py
    #Update transaction table
    datenow = date.today
    trans = Transaction() 
    if host_id:
        trans.host = host
        trans.enduser = enduser        
        trans.price = amount
        trans.favortype = favortype
        trans.invoice = invoice
        trans.dayrangestart = dayrangestart
        trans.dayrangeend = dayrangeend
        trans.deliverydatenotracking_rangestart = datenow + timedelta(days=3)
        trans.deliverydatenotracking_rangeend = datenow + timedelta(days=4)
    trans.save()
    #context = {"form": form}
    return render(request, 'blocbox/payment.html', {
		    'enduser':enduser, 'host':host, 'invoice': invoice,
    	  'date':date, 'local_timezone':local_timezone, 
    	  'amount':amount, "youselected": youselected,
    	  'dayrangestart': dayrangestart, 'dayrangeend': dayrangeend,
    	  'here': quote(request.get_full_path()), 'form': form,
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

