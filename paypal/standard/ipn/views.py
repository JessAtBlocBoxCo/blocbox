#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Generic Stuff
from django.http import HttpResponse, QueryDict, Http404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, render_to_response
#Import IPN model andn forms
from paypal.standard.ipn.forms import PayPalIPNForm
from paypal.standard.ipn.models import PayPalIPN
#Scheduling Stuff
import datetime
import pytz
from urllib import quote


@require_POST
@csrf_exempt
def ipn(request, item_check_callable=None):
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

        form = PayPalIPNForm(data)
        if form.is_valid():
            try:
                #When commit = False, object is returned without saving to DB.
                ipn_obj = form.save(commit=False)
            except Exception as e:
                flag = "Exception while processing. (%s)" % e
        else:
            flag = "Invalid form. (%s)" % form.errors

    if ipn_obj is None:
        ipn_obj = PayPalIPN()

    #Set query params and sender's IP address
    ipn_obj.initialize(request)

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
def ask_for_money(request, host_id=None, paymentoption="package"): #default amount is 2.00
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    date = timezone.now()
    if paymentoption=="bundle10":
        amount="15.00"
        youselected="Bundle of 10 Packages"
    elif paymentoption=="month20":
        amount="15.00"
        youselected="Monthly"
    elif paymentoption=="annual":
        amount="150.00"
        youselected="Annual"
    else:
        amount="2.00"
        youselected="Per Package"
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL, #this is currently defined as jessica.yeats@gmail.com
        "amount": amount, #Amount of the purchase - try to pass this as an argument
        "item_name": "Package",
        "invoice": "UPDATE-PASS-UNIQUE-ID",
        #need keywords for that reverse
        "notify_url": "http://www.blocbox.co" + reverse('payment:paypal_ipn_notify'),
        #"notify_url": "www.blocbox.co" + reverse('payment:paypal_ipn', kwargs={'host_id':host_id, 'paymentoption':paymentoption}), 
        #"notify_url": "https//www.blocbox.co" + reverse('payment:paypal_ipn', kwargs={'host_id':host_id, 'paymentoption':paymentoption}), #this corresponds to the paypal_ipn - blocbox.co/payment/ipn/notify
        "return_url": "http://www.blocbox.co/dashboard/",
        "cancel_return": "http://www.blocbox.co/dashboard/",
    }    
    form = PayPalPaymentsForm(initial=paypal_dict) #in paypal/standard/forms.py
    #context = {"form": form}
    return render(request, 'blocbox/payment.html', { 
		    'enduser':enduser, 'host':host,
    	  'date':date, 'local_timezone':local_timezone, 
    	  'amount':amount, "youselected": youselected,
    	  'here': quote(request.get_full_path()), 'form': form,
    })
    
"""Need to implement a return view and a cancel view, from documentation:
 	You will also need to implement the 'return_url' and 'cancel_return' views
   to handle someone returning from PayPal. Note that these views need
   @csrf_exempt applied to them, because PayPal will POST to them, so they
   should be custom views that don't need to handle POSTs otherwise.

   For 'return_url' you need to cope with the possibility that the IPN has not
   yet been received and handled by the IPN listener you implemented (which can
   happen rarely), or that there was some kind of error with the IPN."""

