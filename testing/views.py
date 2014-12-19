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
#from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
#from CORE and TRANSACTION
from core.models import UserInfo
from connections.models import Connection
from core.forms import UserForm, HostForm
from transactions.models import Transaction
#from schedule import periods
from schedule.periods import Month
from schedule.periods import weekday_names
from schedule.conf.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT
from schedule.forms import EventForm, OccurrenceForm
from schedule.models import Calendar, Occurrence, Event
from schedule.models.calendars import CalendarRelation
from schedule.utils import check_event_permissions, coerce_date_dict
#Import Payment Stuff
from paypal.standard.ipn.models import PayPalIPN

#Write a custom template filter:
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


#define the dashboard test
def dashboard_test(request, host_id=None):
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    connections_all = Connection.objects.filter(end_user=enduser) 
    #lists of transactions
    transactions_all = PayPalIPN.objects.filter(custom=enduser.email) #custom is the field for user email
    shipments_all = transactions_all.filter(item_name="package")
    otherfavors_all = transactions_all.exclude(item_name="package")
    #shipments_all = PayPalIPN.objects.filter(custom=enduser.email) #custom is the field for user email
    return render(request, 'testing/dashboard.html', {
        'enduser': enduser, 'host': host,
        'connections_all': connections_all, 
        'transactions_all': transactions_all, 'shipments_all': shipments_all, 'otherfavors_all': otherfavors_all,
    })



    
#www.blocbox.co/testing/jessstes; .blocbox.co/testing/jesstest/host2/ is to link it to a host's cal
# rendering calendar, note that claneder_slug is passed as argument in URL in base scheduling app
def jesscaltest(request, host_id=None): # calendar_slug_single = "testcalendar1", 
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    connections_all = Connection.objects.filter(end_user=enduser) 
    #I am copying the following date passing arguments from the calendar_by_periods function in schedule/views.py.. but i want to know how to just call that here   
    #calndar stuff initially defined in schedule.views.calendar_by_periods    
    #get the date -- coudl also do this with date = datetime.datetime.now()
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
    #calendar_single = get_object_or_404(Calendar, slug=calendar_slug_single) #this is working
    #event_list_single = GET_EVENTS_FUNC(request, calendar_single)  #this is working 
    #thismonth_object_single = Month(event_list_single, date, None, None, local_timezone) #specific to the calendar  
    #Show all calendars associated with a particular host, host_id is currently defined above when called - want to pass it in URL
    cal_relations_all = CalendarRelation.objects.all() #this is a list of CalendarRelation objects
    cal_list_host = []
    if host:
        cal_relations_host = CalendarRelation.objects.filter(object_id=host.id)
        cal_relations_host_count = CalendarRelation.objects.filter(object_id=host.id).count()
        for cal in cal_relations_host:
            cal_list_host.append(get_object_or_404(Calendar, id=cal.calendar_id))
        AvailabilityCal_Slug = "AvailabilityUser" + str(host.id)
        AvailabilityCal = get_object_or_404(Calendar, slug=AvailabilityCal_Slug)
        AvailabilityCal_EventList = GET_EVENTS_FUNC(request, AvailabilityCal)
        AvailabilityCal_MonthObject = Month(AvailabilityCal_EventList, date, None, None, local_timezone)
    else:
        cal_relations_host = None
        cal_relations_host_count = None
    return render(request, 'testing/jesstest.html', { 
        'enduser':enduser, 'host':host, 
        'connections_all':connections_all,
    	  'date':date,     	   
    	  #'thismonth_object_single':thismonth_object_single, 'calendar_single': calendar_single,
    	  'thismonth_objects':thismonth_objects, 'thismonthname':thismonthname, 'weekday_names': weekday_names,
        'cal_list':cal_list, 'calendar_objects':calendar_objects,  
    	  'cal_relations_all': cal_relations_all, 'cal_relations_host': cal_relations_host,
    	  'cal_relations_host_count': cal_relations_host_count,
    	  'cal_list_host': cal_list_host, 
    	  'AvailabilityCal': AvailabilityCal, 'AvailabilityCal_MonthObject': AvailabilityCal_MonthObject,
    	  'here': quote(request.get_full_path())
    }) 

#bootsrap test - copy of the waitlist sign-up page
def bootstraptest(request):
    return render(request, 'blocbox/x_bootstraptest.html') 

#style tests
def styletest(request):
    return render(request, 'blocbox/x_styletest.html') 
    
"""
JMY NOTE ON DICTIONARIES VERSUS  LISTS:
    Lists: 	a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. 
    				You can remove values from the list, and add new values to the end. Example: Your many cats' names.
    				
    				cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
    				
    Tuples: like lists but you can't change their values. 
    				The values that you give it first up, are the values that you are stuck with for the rest of the program. 
    				Again, each value is numbered starting from zero, for easy reference. Example: the names of the months of the year.
    				
    				months = ('January','February','March','April','May','June', 'July','August','September','October','November','  December')

    Dictionaries: You have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - tare similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. You can add, remove, and modify the values in dictionaries. Example: telephone book.

"""

"""
def denyrequestconnect(request, host_id, user_id):
#url(r'^email/(?P<userinfo_id>\d+)/requestconnectdeny/(?P<userinfo_id>\d+)/$', views.denyrequestconnect, name='denyrequestconnect'),
    context = RequestContext(request)
    host = get_object_or_404(UserInfo, pk=host_id)
    enduser = get_object_or_404(UserInfo, pk=user_id)
"""
