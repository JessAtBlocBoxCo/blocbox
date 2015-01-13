#This is blocbox.transactions.views.py
from django.shortcuts import render
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
#from core and TRANSACTION models
from core.models import UserInfo
from connections.models import Connection
from core.forms import UserForm, HostForm
from transactions.models import Transaction
#billing and payment stuff to import
from billing import gateway, CreditCard
from paypal.standard.forms import PayPalPaymentsForm



#Add the base view -- this is before they have selected the produce/before pricing information is submitted
def base(request, host_id=None, dayrangestart=None, dayrangeend=None):
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    date = timezone.now()
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    return render(request, 'blocbox/payment.html', { 
		    'enduser':enduser, 'host':host,
    	  'date':date, 'local_timezone':local_timezone, 
    	  'dayrangestart': dayrangestart, 'dayrangeend': dayrangeend,
    	  'here': quote(request.get_full_path())
    })

#paypal_ipn views at blocbox/paypal/standard/ipn/views.py