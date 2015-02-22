#import scheduling stuff
import datetime
import pytz
from urllib import quote
from django.conf import settings
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
#import new homebrew calendar
from calendar_homebrew.models import HostConflicts, HostWeeklyDefaultSchedule
import calendar #REMEMBER TO DO THIS!!
calendar.setfirstweekday(6) #Set first weekday: 6 is sunday, 0 is monday, default is 0/monday
#Write a custom template filter:
from django.template.defaulttags import register
#Define general date vars to use in lots of functions
date_today = datetime.date.today()
datetime_now = datetime.datetime.now()
thisyear = date_today.year
nextyear = date_today.year + 1
thisyear_isleap = calendar.isleap(thisyear)
nextyear_isleap = calendar.isleap(nextyear)
thismonth_num = date_today.month  
thismonth_calendar = calendar.monthcalendar(thisyear, thismonth_num)
if thismonth_num == 12:
    nextmonth_num = 1
else:
    nextmonth_num = date_today.month + 1
nextmonth_calendar = calendar.monthcalendar(thisyear, nextmonth_num)
thismonth = calendar.month_name[thismonth_num]
nextmonth = calendar.month_name[nextmonth_num]
monthrange_thismonth = calendar.monthrange(thisyear, thismonth_num)
monthrange_nextmonth = calendar.monthrange(thisyear, nextmonth_num)
days_in_thismonth = monthrange_thismonth[1]
days_in_nextmonth = monthrange_nextmonth[1]
firstweekday_num = calendar.firstweekday()
firstweekday = calendar.day_name[firstweekday_num]
weekheader_chars = 3
weekheaders = calendar.weekheader(weekheader_chars) #(n) specifies the width in characgters for one weekday 
today_dayofmonth_num = date_today.day
today_dayofweek_num = date_today.weekday()
today_dayofweek_name =  calendar.day_name[today_dayofweek_num] #day name is san array 
today_dayofweek_abbr = calendar.day_abbr[today_dayofweek_num] 
#AFTERSHIP API STUFF
import aftership
AFTERSHIP_API_KEY = settings.AFTERSHIP_API_KEY #DEFINED IN SETTINGS.PY
api = aftership.APIv4(AFTERSHIP_API_KEY) #Defined in settings.py
couriers = api.couriers.all.get()
#Create empty list variab les
shipments_with_tracking_allpaid = []                 
shipments_with_tracking_complete = []                
shipments_with_tracking_notcomplete = []             
shipments_with_tracking_notcomplete_delivered = []   
shipments_with_tracking_notcomplete_notdelivered = []
shipments_with_tracking_notcomplete_notrackingno = []

#Define get_item function
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def facebook(request):
    enduser = request.user
    if request.method == 'POST':
        data = request.POST.get('data')
        if enduser.is_authenticated():
            user = get_object_or_404(UserInfo, pk=enduser.id)
            user.facebook_id = data.facebook_id
            user.save()
        else:
           return HttpResponse("The user is not authenticated/ post method failed")
    return render(request, 'testing/facebooklogin.html', {'enduser': enduser,    })

def sendfacebookdata(request):
    enduser = request.user
    if request.method == 'GET':
        return HttpResponse("OK")
    elif request.method == 'POST':
        ## access you data by playing around with the request.POST object
        data = request.POST.get('data')
        if enduser.is_authenticated():
            user = get_object_or_404(UserInfo, pk=enduser.id)
            user.facebook_id = data.facebook_id
            #user.facebook_locale = data.facebook_response.locale
            user.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("OK")
	 

def aftership(request):
    enduser = request.user
    if enduser.is_authenticated():
        transactions_all = Transaction.objects.filter(enduser=enduser) #custom is the field for user email
        transactions_all_paid = transactions_all.filter(payment_processed=True)
        shipments_all_paid = transactions_all_paid.filter(favortype="package")
        otherfavors_all_paid = transactions_all_paid.exclude(favortype="package")
        #Merge the shipments table dta with the aftership API data in lists called 'shipmetns_with_tracking'
   	    #Noet that with_trackign means it has tracking information appended - does not mean it is on aftership or has a trackin gnumber, that could be empty      
        for shipment in shipments_all_paid:  
            tracking_no = str(shipment.tracking) #the str function removes the preceding u'
            shipment_tuple = {} 
            shipment_tuple['trans']=shipment #get all of the transaction variables
            shipment_tuple['aftership']={}  
            if shipment.on_aftership: 
                #populate the aftership_tracking sub-tuble                 
                courier_allfields = api.couriers.detect.post(tracking=dict(tracking_number=tracking_no))
                courier_list = courier_allfields.get(u'couriers')
                courier_list_first = courier_list[0]
                slug_to_detect_u = courier_list_first.get(u'slug')
                slug_to_detect = str(slug_to_detect_u)
                datadict = api.trackings.get(slug_to_detect, tracking_no)
                shipment_tuple['aftership'] = datadict.get(u'tracking') 
                #extract date-only form of expected delivery 
                expected_delivery = shipment_tuple['aftership']['expected_delivery']
                if expected_delivery:
                    shipment_tuple['aftership']['expected_delivery_notime']=expected_delivery.date()
                else:
                    shipment_tuple['aftership']['expected_delivery_notime']=None  
                checkpoints = shipment_tuple['aftership']['checkpoints']
                if checkpoints:
                    shipment_tuple['aftership']['checkpoints'] = checkpoints
                    shipment_tuple['aftership']['last_checkpoint'] = checkpoints[-1] #-nth to last.. so -1 is the last element     
                if shipment.trans_complete ==True:
                    shipments_with_tracking_complete.append(shipment_tuple)
                else:
                    shipments_with_tracking_notcomplete.append(shipment_tuple)
                    tag = shipment_tuple['aftership']['tag']
                    if tag == "Delivered":
                        shipments_with_tracking_notcomplete_delivered.append(shipment_tuple)
                    else:
                        shipments_with_tracking_notcomplete_notdelivered.append(shipment_tuple)
            else: #if not on aftership
                shipment_tuple['aftership']=None
                shipment_tuple['tracking']=None
                if shipment.trans_complete == False:
                    shipments_with_tracking_notcomplete_notrackingno.append(shipment_tuple)
            shipments_with_tracking_allpaid.append(shipment_tuple)
    else: #if not authenticated set these to None
        connections_all = None
        connections_count = None
        hostonly=None
        shipments_all_paid = None
        otherfavors_all_paid = None	  
    return render(request, 'testing/aftership.html', {'enduser': enduser,
        #shipments lists
        'shipments_with_tracking_allpaid': shipments_with_tracking_allpaid, 'shipments_with_tracking_complete': shipments_with_tracking_complete, 
        'shipments_with_tracking_notcomplete': shipments_with_tracking_notcomplete, 
        'shipments_with_tracking_notcomplete_delivered': shipments_with_tracking_notcomplete_delivered, 'shipments_with_tracking_notcomplete_notdelivered': shipments_with_tracking_notcomplete_notdelivered,
        'shipments_with_tracking_notcomplete_notrackingno': shipments_with_tracking_notcomplete_notrackingno,
        #other favors lists
        'otherfavors_all_paid': otherfavors_all_paid, 
    })

    	
#new conflict/scheduling app
#calendar vars: https://docs.python.org/2/library/calendar.html#calendar.month_name
def homebrew_cal(request):
    host = request.user
    #Get calendar_homebrew created fields
    conflicts = HostConflicts.objects.filter(host=host)
    conflicts_date_from = []
    conflicts_startmonths = []
    conflicts_startthismonth = []
    conflicts_startnextmonth = []
    conflicts_startandend_thismonth = []
    conflicts_startandend_nextmonth = []
    conflicts_startthismonth_endnextmonth = []
    conflicts_startthismonth_endlater = []
    conflicts_startnextmonth_endlater = []
    test_list = []
    for conflict in conflicts:  
        start_month = conflict.date_from.month #date_from.month, this is an integer
        if conflict.date_to:
            end_month = conflict.date_to.month
        else:
            end_month = None
        conflicts_startmonths.append(start_month) 
        if start_month == thismonth_num:
            conflicts_startthismonth.append(conflict)
            if start_month == end_month:
                conflicts_startandend_thismonth.append(conflict)
            else:
                if end_month == start_month + 1:
                    conflicts_startthismonth_endnextmonth.append(conflict)
                else:
                    conflicts_startthismonth_endlater.append(conflict)
        if start_month == nextmonth_num:
            conflicts_startnextmonth.append(conflict)
            if start_month == end_month:
                conflicts_startandend_nextmonth.append(conflict)
            else:
                conflicts_startnextmonth_endlater.append(conflict)
    #define days with conflicts
    days_withconflicts_thismonth = []
    days_withconflicts_nextmonth = []
    days_withconflicts_later = []
    for conflict in conflicts_startthismonth:
        #append the first day
        days_withconflicts_thismonth.append(conflict.date_from.day)   
        #append the days after the first day for multi-day conflicts 	  
        if conflict.duration > 1:
            duration_less1 = conflict.duration - 1
            for day in range(duration_less1):
                conflict_day = conflict.date_from.day + day + 1 #range starts at zero so have to add 1
                if conflict_day <= days_in_thismonth:
                    days_withconflicts_thismonth.append(conflict_day)
                else:
                    conflict_day_spillover = conflict_day - days_in_thismonth
                    days_withconflicts_nextmonth.append(conflict_day_spillover)
    for conflict in conflicts_startnextmonth:
    	  #append the first day
        days_withconflicts_thismonth.append(conflict.date_from.day)   
        #append the days after the first day for multi-day conflicts 	  
        if conflict.duration > 1:
            duration_less1 = conflict.duration - 1
            for day in range(duration_less1):
                conflict_day = conflict.date_from.day + day + 1 #range starts at zero so have to add 1
                if conflict_day <= days_in_nextmonth:
                    days_withconflicts_nextmonth.append(conflict_day)
                else:
                    conflict_day_spillover = conflict_day - days_in_thisnext
                    days_withconflicts_later.append(conflict_day_spillover)
    #remove duplciates - hopefully they dont exist but the might          
    days_withconflicts_thismonth = list(set(days_withconflicts_thismonth))
    days_withconflicts_nextmonth = list(set(days_withconflicts_nextmonth))
    #Schedulign fields from user's schedule table
    schedule_list = HostWeeklyDefaultSchedule.objects.filter(host=host)
    schedule = schedule_list[0]
    return render(request, 'testing/homebrew_calendar.html', { 'host': host, 
        #pass calendar fields
    	  'conflicts': conflicts, 'conflicts_startthismonth': conflicts_startthismonth, 'conflicts_startnextmonth': conflicts_startnextmonth, 
    	  'conflicts_startandend_thismonth': conflicts_startandend_thismonth, 'conflicts_startandend_nextmonth': conflicts_startandend_nextmonth,
    	  'days_withconflicts_thismonth': days_withconflicts_thismonth, 'days_withconflicts_nextmonth': days_withconflicts_nextmonth,      	  
    	  #pass schedul fields
    	  'schedule': schedule, 
        #pass datefields
        'date_today': date_today, 'datetime_now': datetime_now,  
        #year variables
        'thisyear': thisyear, 'nextyear': nextyear, 'thisyeaer_isleap': thisyear_isleap, 'nextyear_isleap': nextyear_isleap,
        #Month variables
        'thismonth': thismonth,  'nextmonth': nextmonth, 'thismonth_calendar': thismonth_calendar, 'nextmonth_calendar': nextmonth_calendar,
        'monthrange_thismonth': monthrange_thismonth, 'monthrange_nextmonth': monthrange_nextmonth, 'days_in_thismonth': days_in_thismonth, 'days_in_nextmonth': days_in_nextmonth,
        #Week variables
        'firstweekday': firstweekday,  'weekheaders': weekheaders, 
        #DAy variables
        'today_dayofmonth_num': today_dayofmonth_num, 'today_dayofweek_num': today_dayofweek_num, 'today_dayofweek_name': today_dayofweek_name, 
        'today_dayofweek_abbr': today_dayofweek_abbr,        
    })  
    	
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
        AvailabilityCal = None
        AvailabilityCal_MonthObject = None
        cal_relations_host = None
        cal_relations_host_count = None
    #test the API
    #load Transacton table instead of paypal tabl
    transactions_all = Transaction.objects.filter(enduser=enduser) #custom is the field for user email
    shipments_all = list(transactions_all.filter(favortype="package").order_by('id'))
    otherfavors_all = transactions_all.exclude(favortype="package")

    #ISSU - WHAT ABOUT WHEN I DONT KNOW THE SLUG??
    number_to_track = '591099350463' #this is DHL-global-mail
    slug_to_track = 'dhl-global-mail'
    number_get_tracking = '591099350463' #an amazon order i have in process, fedex
    slug_get_tracking = 'fedex' #i am entering a fedex test number
    number_change = '9405510200881439521016'  #usps
    number_delete = '9114901159818233737712' #usps
    slug_modify = 'usps'
		# create tracking: https://www.aftership.com/docs/api/4/trackings/post-trackings
    #api.trackings.post(tracking=dict(slug=slug_to_track, tracking_number=number_to_track, title="Test Title for Create Tracking")) 
    # get tracking by slug and number, return 'title' and 'created_at' field: https://www.aftership.com/docs/api/4/trackings/get-trackings-slug-tracking_number
    #Notice that you can always use/:id to replace /:slug/:tracking_number -- .g. DELETE /trackings/:id
    # all of the fields: 
    #From https://www.aftership.com/docs/api/4/trackings/get-trackings, Fields to include: title,order_id,tag,checkpoints, checkpoint_time, message, country_name
    #Try this: {u'resource': u'/v4/tracking/fedex/591099350463?fields=shipment_type'}}
    #These fields correspond to a URL?, base URL (in __init__.py:  base_url='https://api.aftership.com, then these render as https://api.aftership.com/v4/tracking
    #If i try to access the url it tells me my API key is invalid - how to pass hte API key as an arg?.
    datadict_single = api.trackings.get(slug_get_tracking, number_get_tracking) #all information - not all tracking  
    trackingdict_single = datadict_single.get(u'tracking') #this gets the value of the TRACKING dictionary - which contains all of the fields. yay!!!
    datadict_all = api.trackings.get()
    trackingdict_all = datadict_all.get(u'trackings')
    courier_single_allfields = api.couriers.detect.post(tracking=dict(tracking_number='591099350463')) # api.Courier.detect(number_to_track)
    courier_single_list = courier_single_allfields.get(u'couriers')
    courier_single = courier_single_list[0]
    courier_single_slug = courier_single.get(u'slug')
    courier_slugs = {}
    tracking_numbers = {}
    courier_infos = {}
    trackingdict = {}     
    shipments_with_tracking = [] #WHAT STRUCTURE SHOULD BE: [  {'shipment_id': value, 'shipment_host': value, 'shipment_tracking': {'tracking_ship_date': value, 'expected_delivery': value }}]
    for shipment in shipments_all:  
        tracking_no = str(shipment.tracking) #the str function removes the preceding u'
        shipment_tuple = {} 
        shipment_tuple['id'] = shipment.id
        shipment_tuple['host'] = shipment.host
        shipment_tuple['enduser']=shipment.enduser
        shipment_tuple['invoice']=shipment.invoice
        shipment_tuple['tracking']=tracking_no
        shipment_tuple['price']=shipment.price
        shipment_tuple['dayrangestart']=shipment.dayrangestart
        shipment_tuple['dayrangeend']=shipment.dayrangeend
        shipment_tuple['date_requested']=shipment.date_requested_notime
        shipment_tuple['trans_complete']=shipment.trans_complete
        shipment_tuple['enduser_rating']=shipment.enduser_rating
        shipment_tuple['enduser_comments']=shipment.enduser_comments
        shipment_tuple['enduser_issue']=shipment.enduser_issue
        shipment_tuple['payment_option']=shipment.payment_option
        shipment_tuple['aftership']={}  
        if shipment.tracking: 
            #populate the aftership_tracking sub-tuble                    
            courier_allfields = api.couriers.detect.post(tracking=dict(tracking_number=tracking_no))
            courier_list = courier_allfields.get(u'couriers')
            if courier_list == []:
                courier_slugs[shipment.id] = None
                tracking_numbers[shipment.id]=None
                courier_infos[shipment.id]=None
                shipment_tuple['aftership']=None
            else:
                courier_for_list = courier_list[0]
                slug_for_list_u = courier_for_list.get(u'slug')
                slug_for_list = str(slug_for_list_u)
                courier_slugs[shipment.id] = slug_for_list 
                tracking_numbers[shipment.id] = str(tracking_no)
                courier_infos[shipment.id] = courier_list
                datadict = api.trackings.get(slug_for_list, tracking_no)
                shipment_tuple['aftership'] = datadict.get(u'tracking')             
        else:
            shipment_tuple['aftership']=None
        shipments_with_tracking.append(shipment_tuple)
    #  datadict = api.trackings.get(SLUG_HOW_TO_DEFINE, shipment.tracking)
    #  trackingdict[shipment.id] = datadict.get(u'tracking') 
    #To see all tracking fields print the variable track_allfields
    #Tracking fields from website
    #tracking fields: created_at, updated_at, tracking_number, slug, active, custom_fields (tuple), custom_name, customer_name, destination_country, emails (list?), expected_delivery
		#tracking fields (cont.) order_id, origin_country_iso3, shipment_package_count, shipment_type, signed_by, smses, source, tag, title, tracked_count, unique_token, checkpoints (list with sub variables)
    # change tracking title: https://www.aftership.com/docs/api/4/trackings/put-trackings-slug-tracking_number
    #api.trackings.put(slug_modify, number_change, tracking=dict(title="Title Test (changed)"))
    # delete tracking: https://www.aftership.com/docs/api/4/trackings/delete-trackings
    #api.trackings.delete(slug_modify, number_delete)
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
    	  'here': quote(request.get_full_path()),
    	  'transactions_all': transactions_all, 'shipments_all': shipments_all, 'otherfavors_all': otherfavors_all,
 				'aftership_api_key':AFTERSHIP_API_KEY, 'couriers': couriers, 'trackingdict_single': trackingdict_single, 'trackingdict': trackingdict, 
 				'datadict_all': datadict_all, 'trackingdict_all': trackingdict_all,
 				'courier_single': courier_single, 'courier_single_slug': courier_single_slug,
        'shipments_with_tracking': shipments_with_tracking, 
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
