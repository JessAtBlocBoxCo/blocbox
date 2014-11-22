#This is blocbox/billing/views.py
#import scheduling stuff
import datetime
import pytz
from urllib import quote
#from django
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.core.mail import send_mail
from django.template import RequestContext, loader #allows it to load templates from blocbox/template
from django.views.generic.list import ListView
from django.utils import timezone
from django.conf import settings
#from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
#from core
from core.models import UserInfo, Transaction, Connection
from core.forms import UserForm, HostForm
#billing specific stuff
from billing import gateway, CreditCard
#from billing.urls import urlpatterns
from paypal.standard.forms import PayPalPaymentsForm


# Added the Following to /blocbox/billig'views.py or wherever you want to use it
#Django-Merchan stuff - from http://django-merchant.readthedocs.org/en/latest/overview.html#overview
"""
g1 = get_gateway("authorize_net")
cc = CreditCard(first_name= "Test", last_name = "User", month=10, year=2011, number="4222222222222", verification_value="100")
response1 = g1.purchase(100, cc, options = {...})
#response1
#{"status": "SUCCESS", "response": <AuthorizeNetAIMResponse object>}
g2 = get_gateway("pay_pal")
response2 = g2.purchase(100, cc, options = {...})
#response2
#{"status": "SUCCESS", "response": <PayPalNVP object>}
"""

#Add the base view -- this is before they have selected the produce/before pricing information is submitted
def base(request, host_id=None):
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    date = timezone.now()
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    return render(request, 'blocbox/payment.html', { 
		    'enduser':enduser, 'host':host,
    	  'date':date, 'local_timezone':local_timezone, 
    	  'here': quote(request.get_full_path())
    })

#paypal_ipn views at blocbox/paypal/standard/ipn/views.py


      


