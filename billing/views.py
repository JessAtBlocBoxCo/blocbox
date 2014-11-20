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
from billing import gateway
from billing import CreditCard
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

#Add the base view -- this doesn't have a form/doesn't allow actual payment
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

#Add the paypal_ipn view: www.blocbox.co/billing
def paypal_ipn(request, host_id=None):
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    date = timezone.now()
    local_timezone = request.session.setdefault('django_timezone', 'UTC') 
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL, #this is currently defined as jessica.yeats@gmail.com
        "amount": "2.00", #Amount of the purchase - try to pass this as an argument
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        #"notify_url": "https://www.blocbox.co" + reverse('paypal-ipn'),
        "return_url": "https://www.blocbox.co/startashipment/",
        "cancel_return": "https://www.blocbox.co/beta/",
    }    
    form = PayPalPaymentsForm(initial=paypal_dict) #in paypal/standard/forms.py
    #context = {"form": form}
    return render(request, 'blocbox/payment.html', { 
		    'enduser':enduser, 'host':host,
    	  'date':date, 'local_timezone':local_timezone, 
    	  'here': quote(request.get_full_path()), 'form': form,
    })

#django-paypal tests = TJOS OS P;D
def paypal_askformoney(request):
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        #"notify_url": "https://www.blocbox.co" + reverse('paypal-ipn'),
        "return_url": "https://www.blocbox.co/startashipment/",
        "cancel_return": "https://www.blocbox.co/your-cancel-location/",
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("billing/paypal.html", context) #dont have to do longer path than this becaue template loader finds them...
  
      
    
#Add the checkout view: www.blocbox.co/billing/checkout, host_id can be passed in URL
def checkout(request, host_id=None): 
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



      
        
         
"""
#jessstest - rendering calendar, note that claneder_slug is passed as argument in URL in base scheduling app
def jesstest(request, calendar_slug_single = "testcalendar1", host_id=None):
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    connections_all = Connection.objects.filter(end_user=enduser) 
    try:
        date = coerce_date_dict(request.GET)
    except ValueError:
        raise Http404
    if date:
        try:
            date = datetime.datetime(**date)
        except ValueError:
            raise Http404
    else:
        date = timezone.now()
        local_timezone = request.session.setdefault('django_timezone', 'UTC')     
    local_timezone = pytz.timezone(local_timezone) #this is working]
    thismonthname = Month(date, None, None, local_timezone) 
    cal_list = Calendar.objects.all()
    calendar_objects = {} 
    event_list_objects = {}
    thismonth_objects = {}
    test_calslugs = []
    for cal in cal_list:
        event_list = GET_EVENTS_FUNC(request, cal)
        calendar_objects[cal.slug] = get_object_or_404(Calendar, slug=cal.slug)
        thismonth_objects[cal.slug] = Month(event_list, date, None, None, local_timezone)
    #for a single calendar called i
    calendar_single = get_object_or_404(Calendar, slug=calendar_slug_single) #this is working
    event_list_single = GET_EVENTS_FUNC(request, calendar_single)  #this is working 
    thismonth_object_single = Month(event_list_single, date, None, None, local_timezone) #specific to the calendar  
    #Show all calendars associated with a particular host, host_id is currently defined above when called - want to pass it in URL
    cal_relations_all = CalendarRelation.objects.all() #this is a list of CalendarRelation objects
    cal_list_host = []
    if host:
        cal_relations_host = CalendarRelation.objects.filter(object_id=host.id)
        cal_relations_host_count = CalendarRelation.objects.filter(object_id=host.id).count()
        for cal in cal_relations_host:
            cal_list_host.append(get_object_or_404(Calendar, id=cal.calendar_id))
    else:
        cal_relations_host = None
        cal_relations_host_count = None
    return render(request, 'blocbox/jesstest.html', { 
        'enduser':enduser, 
        'host':host, 
        'connections_all':connections_all,
    	  'date':date, 
    	  'thismonth_objects':thismonth_objects,
    	  'thismonth_object_single':thismonth_object_single,
    	  'thismonthname':thismonthname,
    	  'weekday_names': weekday_names,
        'cal_list':cal_list,
        'calendar_objects':calendar_objects,
    	  'calendar_single': calendar_single,
    	  'cal_relations_all': cal_relations_all,
    	  'cal_relations_host': cal_relations_host,
    	  'cal_relations_host_count': cal_relations_host_count,
    	  'cal_list_host': cal_list_host,
    	  'here': quote(request.get_full_path())
    }) 
"""


