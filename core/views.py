from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.template import RequestContext, loader #allows it to load templates from blocbox/templates
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
jsonDec = json.decoder.JSONDecoder()
from django.http import QueryDict
#Add CORE and TRANSACTIONS models
from core.models import UserInfo
from connections.models import Connection
from transactions.models import Transaction
#from django.contrib.auth.models import User #dont need this because not using User - maybe why it create table..
from core.forms import UserForm, HostForm, ContactUs, NotificationSettings, ResetPassword, Editprofile
from core.usertasks import add_neighbors_nearby_task, add_neighbors_nearby_waitlist, attribute_referral, attribute_referral_waitlist
from connections.forms import ConnectForm
from transactions.forms import TrackingForm, ModifyTransaction, PackageReceived, EndUserIssue, MessageHost, HostReceived, HostIssue, MessageUser
#adding transactions watch_packages task on 8/30 to update dashboard function
from transactions.tasks import watch_packages
#Add the waitlist app
from waitlist.models import Waitlist
from waitlist.forms import WaitlistFormModel, WaitlistForm
#Important the authentication and login functions -- not sure that i can use with custom model
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
##Adding email functionality (http://catherinetenajeros.blogspot.com/2013/03/send-mail.html)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.list import ListView
#import scheduling stuff
import datetime
datetoday = datetime.date.today()
datetimenow = datetime.datetime.now()
import pytz
import urllib
import urllib2
from itertools import chain
from operator import attrgetter
from urllib import quote
#Removing reference to the scheuld app
#from schedule import periods
#from schedule.periods import Month
#from schedule.periods import weekday_names
#from schedule.conf.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT
#from schedule.forms import EventForm, OccurrenceForm
#from schedule.models import Calendar, Occurrence, Event
#from schedule.models.calendars import CalendarRelation
#from schedule.utils import check_event_permissions, coerce_date_dict
from django.utils import timezone
#Import Payment Stuff
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.views import ask_for_money
#Import Messaging Stuff
from django.contrib import messages
from django_messages.models import Message
from django_messages.forms import ComposeForm
from django_messages.utils import format_quote, get_user_model, get_username_field
from django_messages.views import notify_user_received_message
#aftership
import aftership
AFTERSHIP_API_KEY = settings.AFTERSHIP_API_KEY #DEFINED IN SETTINGS.PY
api = aftership.APIv4(AFTERSHIP_API_KEY) #Defined in settings.py
#pyzipcode
import pyzipcode
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

#################33
#THE FOLLOWING SHIT IS NEEDED FOR THE HOST AVAILABIITY CLANEDAR -- JESS EDITING ON 9/6/2015 E
#import new homebrew calendar
#NOTE - HOSTCONFLICTS_DATEVERSIO IS THE ONE CURRENTLY IN USE
from calendar_homebrew.models import HostConflicts_DateVersion, HostConflicts_DateVersion_OneTable, HostConflicts_OldVersion, HostConflicts_BooleanVersion, HostWeeklyDefaultSchedule
#Import the HostConflictsForm -- i just created this in calendar_homebrew.forms.py
from calendar_homebrew.forms import HostConflictsForm_DateVersion, HostConflictsForm_OldVersion, CalendarCheckBoxes
#Define lots of generic date fields that will be accessed by several functions - note that some of these may already be defined in core.views etc
import calendar 
calendar.setfirstweekday(6) #Set first weekday: 6 is sunday, 0 is monday, default is 0/monday    
date_today = datetime.date.today()
datetime_now = datetime.datetime.now()
time = datetime.datetime.time(datetime_now)
thisyear = date_today.year
nextyear = date_today.year + 1
thisyear_isleap = calendar.isleap(thisyear)
nextyear_isleap = calendar.isleap(nextyear)
thismonth_num = date_today.month  
if thismonth_num == 12:
    nextmonth_num = 1
    nextmonth_calendar_year = nextyear
else:
    nextmonth_num = date_today.month + 1
    nextmonth_calendar_year = thisyear
    thismonth_calendar = calendar.monthcalendar(thisyear, thismonth_num)
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


#DEFINIGN SOME LIST VARSIABLES USED BY SEVERAL VIEWS BELOW
shipments_with_tracking_allpaid = []                 
shipments_with_tracking_complete = []                
shipments_with_tracking_notcomplete = []             
shipments_with_tracking_notcomplete_delivered = []   
shipments_with_tracking_notcomplete_notdelivered = []
shipments_with_tracking_notcomplete_notrackingno = []
shipments_complete_fordash = [] #all ocmplete shipments
shipments_no_tracking_complete = [] #shipments marked as ocmplete that never had trcking
    

    
#Write a custom template filter:
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    

#-------------------------------------------------------------------------
#Waitlist, beta, getting started, about and dashboard/profile pages
#-------------------------------------------------------------------------

#NOTE THIS REFERRAL LINK PROGRAM IS BUILT INTO THE WAITLIST PAGE SUCH THAT IT REDIRECT TO JOHN - SIGNUP/HOST2/ - IN FUTURE WILL WANT
#TO UPDATE THIS IF WE WANT REFERALLS TO HOSTS OTHER THAN JOHN -- SO WE WILL HAVE TO KNOW WHAT HOST THE SUER IS REFERRING TO 
def waitlist(request, referring_user_email=None, neighborhood=None):
    if neighborhood in ("clintonhill", "brooklyn"): 
        host_id = 2 
    else:
        host_id = None
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    if neighborhood == "clintonhill":
        neighborhood_text = "Clinton Hill"
    elif neighborhood == "brooklyn":
        neighborhood_text = "Brooklyn, NY"
    else:
        neighborhood_text = None
    return render(request, 'blocbox/waitlist.html', { 
    		'referring_user_email': referring_user_email, 'neighborhood_text': neighborhood_text, 
            'neighborhood': neighborhood, 'host': host, } ) #loads blocbox/templates/blocbox/waitlist.html 

def beta(request):
    return render(request, 'blocbox/beta.html') #load the blocbox/templates/blocbox/beta.html 

def search(request):
    enduser = request.user
    users_all = UserInfo.objects.all
    hosts_all = UserInfo.objects.filter(host=1)
    hosts_list_onlyjb = hosts_all.filter(id=2)
    return render(request, 'blocbox/search.html', {
        'enduser': enduser, 'hosts_all': hosts_all, 'users_all': users_all, 'hosts_list_onlyjb': hosts_list_onlyjb,   
    })

def search_test(request):
    enduser = request.user
    users_all = UserInfo.objects.all
    hosts_all = UserInfo.objects.filter(host=1)
    hosts_list_onlyjb = hosts_all.filter(id=2)
    return render(request, 'blocbox/old/search_test.html', {
        'enduser': enduser, 'hosts_all': hosts_all, 'users_all': users_all, 'hosts_list_onlyjb': hosts_list_onlyjb,   
    })

def contactus(request):
    enduser = request.user
    recipient = 'admin@blocbox.co'
    if request.method == 'POST': 
        contactus_form = ContactUs(request.POST)       
        if contactus_form.is_valid():
            contactus_subject = contactus_form.cleaned_data['contactus_subject']
            contactus_body = contactus_form.cleaned_data['contactus_body']
            if enduser.is_authenticated():
                sender_info = "User ID " + str(enduser.id) + ": " +str(enduser.first_name) + str(enduser.last_name) + " at " + str(enduser.email) 
                reply_to_email = enduser.email
                isregistered = "The message was sent by a registered user."
            else:
                sender_info = "A Guest User/ Not Authenticated User."
                reply_to_email = contactus_form.cleaned_data['reply_to_email']
                isregistered = "The message was sent by an unregistered user or a user that was not signed in."
            message = render_to_string('emails/notify_admin_contactus.txt', { 
                'enduser': enduser, 'sender_info': sender_info, 'contactus_subject': contactus_subject, 'contactus_body': contactus_body, 
                'reply_to_email': reply_to_email, 'isregistered': isregistered,
            })
            subject = "[CONTACT US]: " + str(reply_to_email) + " has sent a message via the Contact Us/Support Page"
            send_mail(subject, message,  'Blocbox Contact Us <admin@blocbox.co>', ['john@blocbox.co',  'admin@blocbox.co',])
            #return HttpResponse("An email has been sent to the BlocBox team with your message.")
        else:  #if form is not valid
            print contactus_form.errors
    else: #if request is not post
        contactus_form = ContactUs()
    return render(request, 'blocbox/contactus.html', {'enduser': enduser, 'contactus_form': contactus_form,  })
   
   
    
def aboutblocbox(request):
    enduser = request.user
    return render(request, 'blocbox/aboutblocbox.html', {'enduser': enduser,})
    	
def abouthosting(request):
    enduser = request.user
    return render(request, 'blocbox/abouthosting.html', {'enduser':enduser,})

#define the function to send an email to the host that the user has added tracking
def notifyhost_tracking_added(request, thisvariableacceptsthehostinfo, thisvariableacceptstheuserinfo, thisvariableacceptstransactioninfo):
    host = get_object_or_404(UserInfo, pk=thisvariableacceptsthehostinfo)
    enduser = get_object_or_404(UserInfo, pk=thisvariableacceptstheuserinfo)
    trans = get_object_or_404(Transaction, pk=thisvariableacceptstransactioninfo)
    message = render_to_string('emails/notify_host_tracking_added.txt', {'host': host, 'enduser': enduser, 'trans': trans})
    subject = "Your neighbor has added tracking to an incoming delivery!"
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [host.email,])
    
    
#The dashboard function    
def dashboard(request, host_id=None, trans=None, track_id=None, confirm_id=None, issue_id=None, message_trans_id=None, archive_id=None): #modify_id=None
    enduser = request.user
    if host_id: #JB - old host authentification or is it host connection?
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    #if archive_id archive the shipments
    if archive_id: #JB - send shipments to archive
        trans = get_object_or_404(Transaction, pk=archive_id)
        trans.trans_archived=True
        trans.save()
    #variables requiring authentication
    if enduser.is_authenticated(): #JB - user authentication
        connections_all = Connection.objects.filter(end_user=enduser) #JB - displays hosts connected to
        connections_count = connections_all.count() #count them,removing status=0 after host_user=host #JB - displays number of connections (to hosts)
        #determine whether they are only connected to one host for pupose of 'start a shipment' link
        if connections_count==1: #JB - if only one host is connected then it displays the host info
            hostonly=connections_all[0].host_user
        else:
            hostonly=None 
        #First - Call the watch_packages task int ransactions.tasks just for this user
        watch_packages(specificuser_id=enduser.id)
        #Now, load
        transactions_all = Transaction.objects.filter(enduser=enduser) #custom is the field for user email #JB - below is list of catagories and states for shipments
        transactions_all_paid = transactions_all.filter(payment_processed=True)
        shipments_all_paid = transactions_all_paid.filter(favortype="package")
        shipments_all_paid_notarchived = shipments_all_paid.exclude(trans_archived=True)
        shipments_all_paid_notarchived_notcomplete = shipments_all_paid_notarchived.filter(trans_complete=False)
        otherfavors_all_paid = transactions_all_paid.exclude(favortype="package")
        otherfavors_all_paid_notarchived = otherfavors_all_paid.exclude(trans_archived=True)
        #Create lists restricted to shipmetns that are on aftership
        shipments_complete_fordash = shipments_all_paid_notarchived.filter(trans_complete=True)
        #Waiting for Tracking - Shipments that are not archived and not on aftership
        shipments_onaftership_notcomplete_notrackingno = shipments_all_paid_notarchived_notcomplete.filter(on_aftership=False)
        #WAiting for pickup: Create list of shipments that are not archived and not complete
        shipments_onaftership_notarchived_notcomplete = shipments_all_paid_notarchived_notcomplete.filter(on_aftership=True)
        shipments_onaftership_notcomplete_delivered = shipments_onaftership_notarchived_notcomplete.filter(last_tracking_status="Delivered")
        #shipments in transit/not delivered
        shipments_onaftership_notcomplete_notdelivered = shipments_onaftership_notarchived_notcomplete.exclude(last_tracking_status="Delivered")
        #shipments with attempt fail
        shipments_onaftership_notcomplete_notdelivered_fail = shipments_onaftership_notcomplete_notdelivered.filter(last_tracking_status="AttemptFail")
    else: #if not authenticated set these to None
        connections_all = None
        connections_count = None
        hostonly=None
        shipments_all_paid_notarchived = None
        otherfavors_all_paid = None
        otherfavors_all_paid_notarchived = None
        shipments_onaftership_notcomplete_delivered = None
        shipments_onaftership_notcomplete_notdelivered = None
        shipments_onaftership_notcomplete_notrackingno = None
        shipments_complete_fordash = None
        shipments_onaftership_notcomplete_notdelivered_fail = None
    tracking_form = None  #is None if no track_id (if they dont open the modal) 
    if track_id:  #if they open a tracking modal
        track_id_int = track_id.strip()
        track_id_int = int(track_id_int)
        dashboard_tracking_modal(request, track_id) #defined below 
    else:
        track_id_int = None 
    package_received_form = None #is None if they dont open package recieved modal
    if confirm_id:  #if the open the package_received modal #JB - confirming what?
        confirm_id_int = confirm_id.strip()
        confirm_id_int = int(confirm_id_int)
        package_received_modal(request, confirm_id) 	
    else:
        confirm_id_int = None
    enduser_issue_form = None #if they dont open the report an issue modal
    if issue_id:     #if they open the EndUser Issues Modal/Button
        issue_id_int = issue_id.strip()
        issue_id_int = int(issue_id)
        enduser_report_issue_modal(request, issue_id)
    else:
        issue_id_int = None
    message_form = None 
    recipient_email_list = None
    if message_trans_id: #if they open the message host modal
        message_trans_id_int = message_trans_id.strip()
        message_trans_id_int = int(message_trans_id_int)
        message_host_modal(request, message_trans_id)  
    else:
        message_trans_id_int = None   
    return render(request, 'blocbox/dashboard.html', {
        'enduser': enduser, 'host': host, 'datetimenow': datetimenow, 'datetoday': datetoday,
        'connections_all': connections_all, 'connections_count': connections_count,
        'hostonly': hostonly, 'request': request,  'trans': trans, 
        'track_id': track_id, 'track_id_int': track_id_int, 'confirm_id': confirm_id, 'confirm_id_int': confirm_id_int, 
        'message_trans_id': message_trans_id, 'message_trans_id_int': message_trans_id_int, 'issue_id': issue_id, 'issue_id_int': issue_id_int,
        'tracking_form': tracking_form, 'package_received_form': package_received_form, 'enduser_issue_form': enduser_issue_form, 'message_form': message_form, 
        'recipient_email_list': recipient_email_list,
        #shipments lists
        'shipments_onaftership_notcomplete_delivered': shipments_onaftership_notcomplete_delivered, 
        'shipments_onaftership_notcomplete_notdelivered': shipments_onaftership_notcomplete_notdelivered,
        #shipmetns that need tracking
        'shipments_onaftership_notcomplete_notrackingno': shipments_onaftership_notcomplete_notrackingno,
        #all completeshipmetns
        'shipments_complete_fordash': shipments_complete_fordash,
        #other favors lists
        'otherfavors_all_paid': otherfavors_all_paid,
        'shipments_onaftership_notcomplete_notdelivered_fail': shipments_onaftership_notcomplete_notdelivered_fail,    
    })

def enduser_report_issue_modal(request, issue_id):
    trans = Transaction.objects.get(pk=issue_id)
    if request.method == 'POST':
        enduser_issue_form = EndUserIssue(request.POST, instance=trans)
        if enduser_issue_form.is_valid():
            issue = enduser_issue_form.save()
            issue.save()
            notify_host_enduser_issue(request, trans.id)
            notify_admin_enduser_issue(request, trans.id)
        else: 
            print enduser_issue_form.errors
    else:
        enduser_issue_form = EndUserIssue(instance=trans)
    return HttpResponse("OK")

def notify_host_enduser_issue(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    message = render_to_string('emails/notify_host_enduser_issue.txt', 
        { 'host': host, 'enduser': enduser, 'trans': trans})
    subject = "Your Neighbor " + str(enduser.first_name) + " has reported an issue with Order " + str(trans.id)
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [host.email,]) #last is the to-email
    return HttpResponse("An email has been sent to the host to notify them about this issue.")

def notify_admin_enduser_issue(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    message = render_to_string('emails/notify_admin_enduser_issue.txt', 
        { 'host': host, 'enduser': enduser, 'trans': trans})
    subject = "[ENDUSER_ISSUE]: User " + str(enduser.email) + " has reported an issue with Order " + str(trans.id)
    send_mail(subject, message, 'BlocBox EndUser Issues <admin@blocbox.co>', ['john@blocbox.co', 'admin@blocbox.co',]) #last is the to-email
    return HttpResponse("An email has been sent to the BlocBox team to notify them about this issue.")
    
def message_host_modal(request, message_trans_id):
    trans = Transaction.objects.get(pk=message_trans_id)
    recipient_email = trans.host.email
    recipient_email_list = []
    recipient_email_list.append(recipient_email)
    sender = request.user
    if request.method == 'POST':
        compose_form = ComposeForm(request.POST, recipient_filter=None) #maybe update recipient filter so it goes to the host in question, or can just use trans.host.id        
    		#Add recipient here?
        if compose_form.is_valid(): 
            body = compose_form.cleaned_data['body']
            subject = compose_form.cleaned_data['subject']
            compose_form.save(sender=request.user)            
            for recipient in recipient_email_list:
                notify_user_received_message(request, sender.id, recipient_email, subject, body) 
        else:
            print compose_form.errors
    else:
        compose_form = ComposeForm(recipient_filter=None)
    return HttpResponse("OK")
    

def dashboard_tracking_modal(request, track_id):
    trans = Transaction.objects.get(pk=track_id)  
    tracking_on_trans = str(trans.tracking)
    api = aftership.APIv4(AFTERSHIP_API_KEY) #Defined in settings.py
    enduser = trans.enduser
    if trans.on_aftership:
        courier_on_trans = str(trans.shipment_courier.lower())
    else:
        courier_on_trans = None
    if request.method == 'POST':        
        tracking_form  = TrackingForm(request.POST, instance=trans)
        if tracking_form.is_valid(): 
            tracking_no_entered = tracking_form.cleaned_data['tracking']
            if tracking_no_entered:
                trackadd = tracking_form.save()          
                trackadd.save() 
                tracking_no_to_add = str(trans.tracking) #retrieve the tracking number we just added to the transaction table
                #Get the courier information
                c_allfields = api.couriers.detect.post(tracking=dict(tracking_number=tracking_no_to_add))                
                c_list = c_allfields.get(u'couriers') #the couriers field from teh tuple, this could be empty
                if c_list == []: #if the courier is not detected
                    c_list_first = None  
                    sorry_message = "Either the tracking number is invalid or the courier is not supported by Aftership."
                    suggested_return_url = 'dashboard'
                    suggested_return_message = "Return to your Dashboard"
                    return render(request, 'blocbox/sorry.html', { 'sorry_message': sorry_message, 
                    		'suggested_return_url': suggested_return_url, 'suggested_return_message': suggested_return_message })
                else:    #if the courier is detected
                    c_list_first = c_list[0] #the first element in the list of couriers, since there is only one
                    slug_detected = str(c_list_first.get(u'slug'))
                    # create tracking at aftership: https://www.aftership.com/docs/api/4/trackings/post-trackings
                    # Change customer_name to hos name
                    if trans.host.first_name:
                        customer_name = str(trans.host.first_name) + " " + str(trans.host.last_name)
                    else:
                        customer_name = str(trans.host.email)   
                    #aftership error codes: https://www.aftership.com/docs/api/4/errors
                    #if enduser.notifyuser_trackinginfo:
                    #    notifyemails = [trans.enduser.email, trans.host.email]
                    #else:
                    notifyemails = [trans.host.email]
                    try:
                        api.trackings.post(tracking=dict(
    		                    slug=slug_detected, tracking_number=tracking_no_to_add,  
    		                    title=str(trans.title) + ": Order " + str(trans.id)+": User " + enduser.email+" to Host " + trans.host.email, 
    		                    order_id=str(trans.id),
    		                    customer_name=customer_name,
    		                    emails = notifyemails,
    		                    custom_fields=dict(Enduser_Recipient_Email=trans.enduser.email, Invoice=trans.invoice)
    		                    #Eventually consider add SMSEs here to add phone notifications - its 4 cents per SMS so may not be worth it
    		                    )) 	
                    except aftership.APIv4RequestException as error: 
                        if error.code() == 4003:
                            sorry_message = "That tracking numbers is already being tracked! Please enter a different tracking number. If you think there's something wrong, contact us at info@blocbox.co."                              
                        elif error.code() == 4005:
                        	  sorry_message = "That tracking numbers is invalid. Please enter a different tracking number. If you think there's something wrong, contact us at info@blocbox.co."
                        else:
                            sorry_message = "Something has gone wrong! Try to re-enter your tracking number. If you can't get this to work, contact us at info@blocbox.co. <br> Error code: " + str(error.code()) + "; Error type: " + error.type() + "; Error Message: " + error.message()
                        return render(request, 'blocbox/sorry.html', {'sorry_message': sorry_message, 
                            	  'suggested_return_url': 'dashboard', 'suggested_return_message': "Return to your Dashboard"})
                    #Get the information from the API (is it posted yet?)
                    #JMY updating this to just reference watch_packages on 9/2/2015 to update all info including for the tracking they just added
                    trans.on_aftership = True
                    trans.shipment_courier = slug_detected.upper()
                    trans.save()
                    watch_packages(specificuser_id=enduser.id)
                    #datadict_added = api.trackings.get(slug_detected, tracking_no_to_add)
                    #tracking_info = datadict_added.get(u'tracking') 
                    #tag = tracking_info['tag']
                    #deliverydate_tracking = tracking_info['expected_delivery']
                    #Save this information to trans table         
                    #trans.last_tracking_status = tag
                    #trans.deliverydate_tracking = deliverydate_tracking
                    #trans.save()
                    #send an email to the host telling them tracking info has been added to shipment
                    notifyhost_tracking_added(request, trans.host.id, trans.enduser.id, trans.id)
            else: #if they entered nothing delete it       
                api.trackings.delete(courier_on_trans, tracking_on_trans)
                trans.tracking = None
                trans.on_aftership = False
                trans.save()               
        else: #if tracking form is not valid 
            print tracking_form.errors 
    else: #if method is not POST
        tracking_form = TrackingForm(instance=trans) 
    return HttpResponse("OK")       


def package_received_modal(request, confirm_id):
    trans = Transaction.objects.get(pk=confirm_id)
    if request.method == 'POST':
        package_received_form = PackageReceived(request.POST) #note this is not a model form
        if package_received_form.is_valid():
            trans.enduser_rating = package_received_form.cleaned_data['enduser_rating']
            trans.enduser_comments = package_received_form.cleaned_data['enduser_comments']
            trans.trans_complete = True
            trans.date_completed = datetoday
            trans.datetime_completed = datetimenow
            trans.save()
            #get last aftership stuff
            courier = trans.shipment_courier
            if courier:
                slug = str(trans.shipment_courier.lower())
                tracking = trans.tracking
                datadict = api.trackings.get(slug, tracking)
                tracking_info = datadict.get(u'tracking') 
                new_status = tracking_info['tag']
                trans.last_tracking_status = new_status            
                last_tracking_unicode = tracking_info['last_updated_at']
                last_tracking_datetime = datetime.datetime.strptime(last_tracking_unicode, '%Y-%m-%dT%H:%M:%S+00:00')
                trans.last_tracking_datetime = last_tracking_datetime
                trans.last_tracking_date = last_tracking_datetime.date()
                trans.save()
                checkpoints = tracking_info['checkpoints']
                if checkpoints:
                    last_checkpoint = checkpoints[-1]
                    last_checkpoint_city = last_checkpoint['city']
                    last_checkpoint_state = last_checkpoint['state']
                    last_checkpoint_datetime = last_checkpoint['checkpoint_time']
                    last_checkpoint_date = last_checkpoint_datetime.date()
                    trans.last_checkpoint_city = last_checkpoint_city
                    trans.last_checkpoint_state = last_checkpoint_state 
                    trans.last_checkpoint_datetime = last_checkpoint_datetime
                    trans.last_checkpoint_date = last_checkpoint_date
                    trans.save()
        else:
            print package_received_form.errors
    else:
    	  package_received_form = PackageReceived()
    return HttpResponse("OK")

#END DASHBOARD DEFS

#HOST DASHBOARD DEFS

def dashboard_host_nothing(request, confirm_id=None):
    thepersonviewingthepage = request.user
    return HttpResponse("this is the dashboard_host_nothing def - delete this")
    
def dashboard_host(request, trans=None, track_id=None, confirm_id=None, issue_id=None, message_trans_id=None, archive_id=None):
    thepersonviewingthepage = request.user
    local_timezone = request.session.setdefault('django_timezone', 'UTC')
    local_timezone = pytz.timezone(local_timezone)
    days_withconflicts_thismonth = []
    days_withconflicts_nextmonth = []
    calendar_submit_button_text = "Submit Updated Availability"
    cal_form_submitted = False
    if thepersonviewingthepage.host == True:
        transactions_all = Transaction.objects.filter(host=thepersonviewingthepage) #custom is the field for user email
        transactions_all_paid = transactions_all.filter(payment_processed=True)
        transactions_count = Transaction.objects.filter(host=thepersonviewingthepage).count() #count all of the transactions
        shipments_all_paid = transactions_all_paid.filter(favortype="package")
        shipments_all_paid_notarchived = shipments_all_paid.exclude(trans_archived=True)
        shipments_all_paid_notarchived_notcomplete = shipments_all_paid_notarchived.exclude(trans_complete=True)
        otherfavors_all_paid = transactions_all_paid.exclude(favortype="package")
        otherfavors_all_paid_notarchived = otherfavors_all_paid.exclude(trans_archived=True)
        #Create lists restricted to shipmetns that are on aftership
        shipments_complete_fordash = shipments_all_paid_notarchived.filter(trans_complete=True)
        shipments_complete_fordash_count = shipments_complete_fordash.count()
        #Shipments in transit
        shipments_in_transit = shipments_all_paid_notarchived_notcomplete.exclude(last_tracking_status="Delivered")
        shipments_in_transit_not_received = shipments_in_transit.filter(host_received_datetime=None)
        shipments_in_transit_no_fails = shipments_in_transit.exclude(last_tracking_status="AttemptFail")
        shipments_in_transit_no_fails_not_received = shipments_in_transit_no_fails.filter(host_received_datetime=None)
        shipment_fail = shipments_in_transit.filter(last_tracking_status="AttemptFail")
        shipment_fail_count = shipment_fail.count()
        shipments_in_transit_not_received_count = shipments_in_transit_not_received.count()
        #Shipments awaiting pickup
        shipments_waiting_pickup_delivered = shipments_all_paid_notarchived_notcomplete.filter(last_tracking_status="Delivered")
        shipments_waiting_pickup_received = shipments_all_paid_notarchived_notcomplete.exclude(host_received_datetime=None)
        shipments_waiting = sorted(chain(shipments_waiting_pickup_delivered, shipments_waiting_pickup_received), key=attrgetter('last_tracking_date'))
        shipments_waiting_count = (chain(shipments_waiting_pickup_delivered, shipments_waiting_pickup_received).count()
        #Host connections
        connections_all = Connection.objects.filter(host_user=thepersonviewingthepage) #JB - displays hosts connected to
        connections_count = Connection.objects.filter(host_user=thepersonviewingthepage).count() #count them,removing status=0 after host_user=host
        conflicts = HostConflicts_DateVersion.objects.filter(host=thepersonviewingthepage)
        for conflict in conflicts:
            if conflict.month == thismonth_num:
                days_withconflicts_thismonth.append(conflict.day)
                if conflict.month == nextmonth_num:
                    days_withconflicts_nextmonth.append(conflict.day)
    else: #if not authenticated set these to None
        transactions_all = None
        transactions_all_paid = None
        shipments_all_paid = None
        shipments_all_paid_notarchived = None
        otherfavors_all_paid = None
        otherfavors_all_paid_notarchived = None   
        shipments_complete_fordash = None
        shipments_complete_fordash_count = None
        shipments_in_transit = None
        shipments_in_transit_not_received_count = None
        shipments_in_transit_no_fails = None
        shipments_in_transit_no_fails_not_received = None
        shipment_fail = None
        shipment_fail_count = None
        shipments_waiting_pickup_delivered = None
        shipments_waiting_pickup_received = None
        shipments_waiting = None
        shipments_waiting_pickup_received_count = None
        connections_all = None
        connections_count = None
        transactions_count = None
        conflicts = None
    host_received_form = None
    if confirm_id:  #if the open the package_received modal #JB - confirming what?
        confirm_id_int = confirm_id.strip()
        confirm_id_int = int(confirm_id_int)
        host_received_modal(request, confirm_id) 	
    else:
        confirm_id_int = None
    if issue_id:     #if they open the Host Issues Modal/Button
        issue_id_int = issue_id.strip()
        issue_id_int = int(issue_id)
        host_report_issue_modal(request, issue_id)
    else:
        issue_id_int = None
        message_form = None
        recipient_email_list = None
    if message_trans_id: #if they open the message host modal
        message_trans_id_int = message_trans_id.strip()
        message_trans_id_int = int(message_trans_id_int)
        message_enduser_modal(request, message_trans_id)  
    else:
        message_trans_id_int = None
    if request.method == 'POST':
        cal_form = CalendarCheckBoxes(data=request.POST)
        if cal_form.is_valid():  
            for daynumber in range(1,32):  #starts at zero otherwise so this will stop at 31 
                conflict_new = HostConflicts_DateVersion()        
                daycheckedmonth1 = cal_form.cleaned_data['month1day'+str(daynumber)]    
                if daycheckedmonth1:
                    #add the conflicts monty, day and year - conflict in this month
                    conflict_new.host = thepersonviewingthepage
                    conflict_new.month = thismonth_num
                    conflict_new.day = daynumber
                    conflict_new.year = thisyear
                    conflict_new.date = str(thisyear) + "-" + str(thismonth_num) + "-" + str(daynumber)
                    conflict_new.save()
                    for daynumber in range(1,32): 
                        conflict_new = HostConflicts_DateVersion()
                        daycheckedmonth2 = cal_form.cleaned_data['month2day'+str(daynumber)] 
                        if daycheckedmonth2:
                            #add the conflicts monty, day and year - conflict in this month
                            conflict_new.host = thepersonviewingthepage
                            conflict_new.month = nextmonth_num
                            conflict_new.day = daynumber
                            conflict_new.year = thisyear
                            conflict_new.date = str(nextmonth_calendar_year) + "-" + str(thismonth_num) + "-" + str(daynumber)  
                            conflict_new.save()                              
                            cal_form_submitted = True
                            #test whether line 401 has error
        else: #if not valid/if there are errors
            print cal_form.errors
    else: #if the method is not POST
        cal_form = CalendarCheckBoxes()   
    return render(request, 'blocbox/dashboard-host.html', {
            'enduser':thepersonviewingthepage,
            #transactions all
            'transactions_all': transactions_all, 
            'transactions_all_paid':  transactions_all_paid,
            'shipments_complete_fordash': shipments_complete_fordash,
            'shipments_complete_fordash_count': shipments_complete_fordash_count,
            'shipments_in_transit': shipments_in_transit,
            'shipments_in_transit_not_received_count': shipments_in_transit_not_received_count,
            'shipments_in_transit_no_fails': shipments_in_transit_no_fails,
            'shipments_in_transit_no_fails_not_received': shipments_in_transit_no_fails_not_received,
            'shipment_fail': shipment_fail,
            'shipments_waiting_pickup_delivered': shipments_waiting_pickup_delivered,
            'shipments_waiting_pickup_received': shipments_waiting_pickup_received,
            'shipments_waiting_pickup_received_count': shipments_waiting_pickup_received_count,
            'shipments_waiting': shipments_waiting,
            #otherfavors all
            'otherfavors_all_paid': otherfavors_all_paid, 
            'otherfavors_all_paid_notarchived': otherfavors_all_paid_notarchived,
            'connections_all': connections_all,
            'connections_count': connections_count,
            'transactions_count': transactions_count,
            'shipment_fail_count':  shipment_fail_count,
            'confirm_id': confirm_id, 
            'confirm_id_int': confirm_id_int,
            'issue_id': issue_id,
            'issue_id_int': issue_id_int,
            'host_received_form': host_received_form,
            'message_trans_id': message_trans_id,
            'message_trans_id_int': message_trans_id_int,
            'cal_form': cal_form,
            #Calendar and date variables
            'local_timezone': local_timezone, 'date_today': date_today, 'datetime_now': datetime_now,  
            'thisyear': thisyear, 'nextyear': nextyear, 'thisyeaer_isleap': thisyear_isleap, 'nextyear_isleap': nextyear_isleap,
            'thismonth': thismonth,  'nextmonth': nextmonth, 'thismonth_calendar': thismonth_calendar, 'nextmonth_calendar': nextmonth_calendar,
            'monthrange_thismonth': monthrange_thismonth, 'monthrange_nextmonth': monthrange_nextmonth, 'days_in_thismonth': days_in_thismonth, 'days_in_nextmonth': days_in_nextmonth, 
            'today_dayofmonth_num': today_dayofmonth_num, 'nextmonth_calendar_year': nextmonth_calendar_year,
            #Unavailable days
            'conflicts': conflicts, 'days_withconflicts_thismonth': days_withconflicts_thismonth, 'days_withconflicts_nextmonth': days_withconflicts_nextmonth,
            'calendar_submit_button_text': calendar_submit_button_text,
})

def host_received_modal(request, confirm_id):
    trans = Transaction.objects.get(pk=confirm_id)
    if request.method == 'POST':
        host_received_form = HostReceived(request.POST) #note this is not a model form
        if host_received_form.is_valid():
            trans.host_received_comments = host_received_form.cleaned_data['host_comments']
            trans.host_received_datetime = datetimenow
            trans.save()
        else:
            print host_received_form.errors
    else:
        host_received_form = HostReceived()
    return HttpResponse("OK")

def host_handoff_modal(request, confirm_id):
    trans = Transaction.objects.get(pk=confirm_id)
    if request.method == 'POST':
        host_handoff_form = HostHandoff(request.POST) #note this is not a model form
        if package_received_form.is_valid():
            trans.host_handoff_comments = host_handoff_form.cleaned_data['host_handoff_comments']
            trans.trans_complete = True
            trans.date_completed = datetoday
            trans.datetime_completed = datetimenow
            trans.save()
            #get last aftership stuff
            courier = trans.shipment_courier
            if courier:
                slug = str(trans.shipment_courier.lower())
                tracking = trans.tracking
                datadict = api.trackings.get(slug, tracking)
                tracking_info = datadict.get(u'tracking') 
                new_status = tracking_info['tag']
                trans.last_tracking_status = new_status            
                last_tracking_unicode = tracking_info['last_updated_at']
                last_tracking_datetime = datetime.datetime.strptime(last_tracking_unicode, '%Y-%m-%dT%H:%M:%S+00:00')
                trans.last_tracking_datetime = last_tracking_datetime
                trans.last_tracking_date = last_tracking_datetime.date()
                trans.save()
                checkpoints = tracking_info['checkpoints']
                if checkpoints:
                    last_checkpoint = checkpoints[-1]
                    last_checkpoint_city = last_checkpoint['city']
                    last_checkpoint_state = last_checkpoint['state']
                    last_checkpoint_datetime = last_checkpoint['checkpoint_time']
                    last_checkpoint_date = last_checkpoint_datetime.date()
                    trans.last_checkpoint_city = last_checkpoint_city
                    trans.last_checkpoint_state = last_checkpoint_state 
                    trans.last_checkpoint_datetime = last_checkpoint_datetime
                    trans.last_checkpoint_date = last_checkpoint_date
                    trans.save()
        else:
            print package_received_form.errors
    else:
        package_received_form = PackageReceived()
    return HttpResponse("OK")

def host_report_issue_modal(request, issue_id):
    trans = Transaction.objects.get(pk=issue_id)
    if request.method == 'POST':
        host_issue_form = HostIssue(request.POST, instance=trans)
        if host_issue_form.is_valid():
            issue = host_issue_form.save()
            issue.save()
            notify_enduser_host_issue(request, trans.id)
            notify_admin_host_issue(request, trans.id)
        else: 
            print enduser_host_form.errors
    else:
        host_issue_form = HostIssue(instance=trans)
    return HttpResponse("OK")

def notify_enduser_host_issue(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    message = render_to_string('emails/notify_enduser_host_issue.txt', 
        { 'host': host, 'enduser': enduser, 'trans': trans})
    subject = "Your Host" + str(host.first_name) + " has reported an issue with Order " + str(trans.id)
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [enduser.email,]) #last is the to-email
    return HttpResponse("An email has been sent to the host to notify them about this issue.")

def notify_admin_host_issue(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    message = render_to_string('emails/notify_admin_enduser_issue.txt', 
        { 'host': host, 'enduser': enduser, 'trans': trans})
    subject = "[HOST_ISSUE]: User " + str(host.email) + " has reported an issue with Order " + str(trans.id)
    send_mail(subject, message, 'BlocBox Host Issues <admin@blocbox.co>', ['john@blocbox.co', 'admin@blocbox.co',]) #last is the to-email
    return HttpResponse("An email has been sent to the BlocBox team to notify them about this issue.")

def message_enduser_modal(request, message_trans_id):
    trans = Transaction.objects.get(pk=message_trans_id)
    host = trans.host
    enduser = trans.enduser
    recipient_email = trans.enduser.email
    recipient_email_list = []
    recipient_email_list.append(recipient_email)
    sender = trans.host
    if request.method == 'POST':
        compose_form = ComposeForm(request.POST, recipient_filter=None) #maybe update recipient filter so it goes to the host in question, or can just use trans.host.id        
            #Add recipient here?
        if compose_form.is_valid(): 
            body = compose_form.cleaned_data['body']
            subject = compose_form.cleaned_data['subject']
            compose_form.save(sender=request.user)            
            for recipient in recipient_email_list:
                notify_user_received_message(request, sender.id, recipient_email, subject, body) 
        else:
            print compose_form.errors
    else:
        compose_form = ComposeForm(recipient_filter=None)
    return HttpResponse("OK")

#END HOST DASHBOARD DEFS
    
def myblock(request):
    return render(request, 'blocbox/myblock.html')
        
def profile(request, user_id):
    enduser = request.user
    return render(request, 'blocbox/profile.html', {'enduser':enduser,})

def editprofile(request, from_page=None):
    enduser=request.user
    if from_page == 'signup':
        fromsignup = True
    else:
        fromsignup = False
    user = get_object_or_404(UserInfo, pk=enduser.id)
    if request.method == 'POST':
        editprofile_form  = Editprofile(request.POST, instance=user) 
        if editprofile_form.is_valid():
            user = editprofile_form.save()
            user.save()
        else:
            print editprofile_form.errors
    else:
        editprofile_form = Editprofile(instance=user)
    return render(request, 'blocbox/editprofile.html', {'enduser': enduser,  'fromsignup': fromsignup, 'from_page': from_page, 
        'editprofile_form': editprofile_form})

def addinterest(request):
    enduser=request.user
    return render(request, 'blocbox/editprofile/addinterest.html', {'enduser': enduser})

def account(request):
    enduser = request.user  
    if enduser.is_authenticated():
        if request.method == 'POST':
            form = NotificationSettings(request.POST, instance=enduser)
            if form.is_valid():
                notify = form.save()
                notify.save()
                user = UserInfo.objects.get(pk=enduser.id)
                mileradius = form.cleaned_data['zipcodes_nearby_mileradius']
                if mileradius == 0:
                    user.notifynotifyuser_newhostonblock = False
                    user.save()
            else: 
                print form.errors
        else:
            form = NotificationSettings(instance=enduser)
    else:
        form = None
    return render(request, 'blocbox/account.html', {'enduser': enduser, 'form': form, })

def paymentoptions(request):
    enduser = request.user
    return render(request, 'blocbox/payment-options.html', {'enduser': enduser,})

def pasttransactions(request):
    enduser = request.user    
    shipments_completed = []                 
    shipments_archived = [] 
    otherfavors_completed = []
    otherfavors_archived = []               
    #variables requiring authentication
    if enduser.is_authenticated():
        transactions_all = Transaction.objects.filter(enduser=enduser)
        transactions_completed = transactions_all.filter(trans_complete=True)
        transactions_archived = transactions_all.filter(trans_archived=True)
        shipments_completed = transactions_completed.filter(favortype="package")
        shipments_archived = transactions_archived.filter(favortype="package")
        otherfavors_completed = transactions_completed.exclude(favortype="package")
        otherfavors_archived = transactions_archived.exclude(favortype="package") 
    else:
        shipments_completed = None
        shipments_archived = None
        otherfavors_completed = None
        otherfavors_archived = None  
        transactions_completed = None
        transactions_archived = None     
    return render(request, 'blocbox/past-transactions.html', {'enduser': enduser, 'shipments_completed': shipments_completed,
    	   'shipments_archived': shipments_archived, 'otherfavors_completed': otherfavors_completed, 'otherfavors_archived': otherfavors_archived, 
    	   'transactions_completed': transactions_completed, 'transactions_archived': transactions_archived, })

def security(request):
    enduser = request.user
    return render(request, 'blocbox/security.html', {'enduser': enduser,})

def settings(request):
    enduser = request.user
    passwordreset_completed = False
    if enduser.is_authenticated():
        user = get_object_or_404(UserInfo, pk=enduser.id)
        if request.method == 'POST': 
            form = ResetPassword(data=request.POST, user=request.user, instance=user)
            if form.is_valid(): 
                user = form.save()
                # Now we hash the password with the set_passworth method, Once hashed, we ca update the user object
                user.set_password(user.password)
                user.save()
                passwordreset_completed = True
            else:
                print form.errors
        else:
            form = ResetPassword(instance=user)
    else:
        form = None
    return render(request, 'blocbox/settings.html', {'enduser': enduser, 'form': form, 'passwordreset_completed': passwordreset_completed })
 
def hostprofile(request, host_id):
    context = RequestContext(request)
    host = get_object_or_404(UserInfo, pk=host_id)
    enduser = request.user
    if enduser.is_authenticated():
        connected = Connection.objects.are_neighbors(user1=enduser, user2=host) #true of false, but not sure how to call thee user...
        enduser_hosts = Connection.objects.enduser_hosts(enduser=enduser)
        enduser_host_connections = Connection.objects.enduser_host_connections(enduser=enduser)
        enduser_is_connected_to_host = Connection.objects.enduser_is_connected_to_host(enduser=enduser, hostuser=host)
    else:
        connected = False
        enduser_hosts = None
        enduser_host_connections = None
        enduser_is_connected_to_host = False
    connections_all = Connection.objects.filter(host_user=host) 
    connections_count = Connection.objects.filter(host_user=host).count() #count them,removing status=0 after host_user=host   
    transactions_all = Transaction.objects.filter(host=host)
    transactions_count = Transaction.objects.filter(host=host).count() #count all of the transactions
    return render_to_response('blocbox/host-profile.html', {'host':host, 'enduser':enduser, 'connected':connected,
    		'connections_all':connections_all, 'connections_count':connections_count, 'connectionstotal':connections_count,
    		'transactions_count':transactions_count, 'transactions_all':transactions_all, 'enduser_hosts':enduser_hosts, 
    		'enduser_host_connections': enduser_host_connections,
    		'enduser_is_connected_to_host': enduser_is_connected_to_host,
    		}, context)

def nudgeaneighbor(request):
    enduser = request.user
    return render(request, 'blocbox/nudge-a-neighbor.html', {'enduser':enduser,})
    	
#-------------------------------------------------------------------------
#Registration and login pages
#-------------------------------------------------------------------------
def userlogin(request):
    context = RequestContext(request)
    badlogin = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/dashboard/') 
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your BlocBox account is disabled.")
        else: # if not user/Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(email, password)
            badlogin = True
            #return HttpResponse("Invalid login details supplied.")
    return render_to_response('blocbox/sign-in.html', {'badlogin': badlogin, }, context)

#logout function
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/beta/')

#Registration Form -- Simple

#Registration Form -- User 
def signup(request, host_id=None, referring_user_email=None, neighborhood=None, hostsignup = False, templatename = 'sign-up-simple'):
    if neighborhood == 'clintonhill':
        host_id = 2 
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    context = RequestContext(request)
    templateloc = 'blocbox/' + templatename + '.html'
    #a bollean value for telling the template whether the registraiton was successful
    #set to false initially; code changes value to True when registraiont succeeds
    registered = False 
    if request.method == 'POST': 
        #if its HTTP post, we're interested in processing form data
    	  # Note that we make user of both userform and UserProfileFrom and HostProfileForm
    	  user_form = UserForm(data=request.POST)  
    	  if user_form.is_valid(): # Check if the form is valid
            # Save the user's form data to the database
            user = user_form.save()
            # Now we hash the password with the set_passworth method; Once hashed, we ca update the user object
            user.set_password(user.password)	
            user.save()
            #get nearby zips and opulate the city and state
            zipcodeform = user_form.cleaned_data['zipcode']
            zipcode = zcdb[zipcodeform]           
            zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 2)]
            zipcodes_nearby_json = json.dumps(zipcodes_nearby)
            user.city = zipcode.city
            user.state = zipcode.state
            user.zipcodes_nearby = zipcodes_nearby_json
            #give all users 1 package credit. if they sign up with a referred by link, give 3 packages credit
            user.account_balance_packages = 1
            if referring_user_email:
                user.account_balance_packages = 3
            #Get naes from full names - comment this out
            #fullname = user_form.cleaned_data['full_name']
            #names = fullname.split(" ")
            #user.first_name = names[0]
            #if len(names) > 1:
            #    user.last_name = names[1]
            #if len(names) > 2:
            #    user.last_name = names[1] + " " + names[2]
            #if hostsignup assign user as host
            if hostsignup:
            	user.host = True
            	user.hostinterest = True
            user.save()
            #add neighbors nearbyu
            add_neighbors_nearby_task(userid=user.id)
            #FILL THIS IN LATER - NEED TO INSTALL THE PIL THING AND ADD A PICTURE FIELD
            #if 'picture' in request.FILES:
            #profile.picture = request.FILES['picture']       	      
            registered = True #Update our variable to tell the template registration was successful        
            #JMY ADDING THESE LINES ON 8/28 TO LOG THEM IN AUTOMATICALLY
            email_entered = user_form.cleaned_data['email']
            password_entered = user_form.cleaned_data['password']
            user_auth_details = authenticate(email=email_entered, password=password_entered)
            login(request, user_auth_details)
            #send an email to the host askig them to confirm the connection
            if host_id:
                confirmconnect_mail(request, host.id, user.id, user.intro_message, user.email, user.first_name, user.last_name) #send a request to connect to the host
                notifyadmin_usersignup(request, host.id, user.id, user.intro_message, user.email, user.first_name, user.last_name) 
                requesthasbeensent(request, host.id, user.id)
            else:
                notifyadmin_usersignup_noconnect(request, user.id, user.intro_message, user.email, user.first_name, user.last_name) 
            if referring_user_email:
                attribute_referral(referring_user_email)
    	  else: 
    	      print user_form.errors
    else:
        user_form = UserForm()
    if registered == True:
        return HttpResponseRedirect('/editprofilefromsignup/')
    else:	
        return render_to_response(templateloc, {'user_form': user_form, 'registered': registered, 'host':host, 'hostsignup': hostsignup,
    	      	'referring_user_email': referring_user_email, }, context)
    	      		
   

    
#OBE - NEED TO REMOVE
def signuplong_host(request):
    context = RequestContext(request)
    registered = False 
    hostsignup = True
    usersignup = False
    if request.method == 'POST':
        host_form = HostForm(data=request.POST)
        if host_form.is_valid():
            host = host_form.save() #save the hosts form data to the database
            host.save() #Save the HostProfile model instance
            registered = True   	  
    	  #Invalid form or forms - print problems to the terminal so they're show to user
        else: 
    	      print host_form.errors
    
    #Not a HTTP Post, so render our form using tow ModelForm instances, will be blank, reader for use rinput   
    else:
        host_form = HostForm()

    return render_to_response(
            'blocbox/signuplong/sign-up-host.html',
    	      {'host_form': host_form, 'registered': registered, 'hostsignup': hostsignup, 'usersignup': usersignup},
    	      context)




#Connet to a new host if already an authenticated user
def connectnewhost(request, host_id):
    enduser = request.user
    host = get_object_or_404(UserInfo, pk=host_id)
    context = RequestContext(request)
    requested = False 
    if request.method == 'POST':        
        connect_form = ConnectForm(data=request.POST)  
        if connect_form.is_valid(): 
            connect = connect_form.save()
            #connect.host_user = host
            #connect.end_user = enduser           
            connect.save()   	 
            requested = True     
            confirmconnect_mail(request, host.id, enduser.id, enduser.intro_message, enduser.email, enduser.first_name, enduser.last_name) #send a request to connect to the host
            #send a email to the enduser/ person requesting to connect thakign them for registering and telling them the request was sent
            requesthasbeensent(request, host.id, enduser.id)
    	  #Invalid form or forms - print problems to the terminal so they're show to user
        else: 
    	      print connect_form.errors    	  
    #If Not a HTTP POST, so we render our form using ModelForm instances - these forms will be blank, ready for user input
    else:
        connect_form = ConnectForm()
    return render_to_response('blocbox/connect-already-registered.html', 
        {'host':host, 'enduser': enduser, 'connect_form': connect_form, 'requested': requested, },context) 

#-------------------------------------------------------------
#Emails
#-------------------------------------------------------------

#simple mail
def typical_mail(request, userinfo_id):
    host = get_object_or_404(UserInfo, pk=userinfo_id)
    message = "Test Simple Mail Message - defined in core/views.py def typical_mail"
    subject = "Test Subject for Simple Mail"
    #from email should be default email defined in settings.py: admin@blocbox.co
    send_mail(subject, message, 'admin@blocbox.co', [host.email,]) #last is the to-email

#using .txt file and passing value(s)    
def confirmconnect_mail(request, hostid, userid, messagetohost, useremail, firstname, lastname):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=userid)
    message = render_to_string('emails/requestconnect.txt', { 'host': host, 'enduser': enduser, 'emailgreeting': messagetohost, 
    	'useremail': useremail, 'firstname':firstname, 'lastname':lastname,})
    subject = "You have a new request to connect from a neighbor"
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [host.email,]) #last is the to-email
    return HttpResponse("An email has been sent to the host to request to connect.")

def notifyadmin_usersignup(request, hostid, userid, messagetohost, useremail, firstname, lastname):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=userid)
    referredby = enduser.referredby
    if referredby:
    	  ref_message = "The User was referred by " + referredby + "."
    else:
      ref_message = None
    message = render_to_string('emails/notifyadmin_usersignup.txt', { 'host': host, 'enduser': enduser, 'emailgreeting': messagetohost, 
    	'useremail': useremail, 'firstname':firstname, 'lastname':lastname, 'ref_message': ref_message, })
    subject = "A New User Has Registered (Full User) - With Request to Connect "
    send_mail(subject, message, 'Blocbox User Registration <admin@blocbox.co>', ['admin@blocbox.co',]) 
    return HttpResponse("An email has been sent to admin@blocbox.co notifying the blocbox team of the new user.")

def notifyadmin_usersignup_noconnect(request, userid, messagetohost, useremail, firstname, lastname):
    enduser = get_object_or_404(UserInfo, pk=userid)
    referredby = enduser.referredby
    if referredby:
        ref_message = "The User was referred by " + referredby + "."
    else:
        ref_message = None
    message = render_to_string('emails/notifyadmin_usersignup_noconnect.txt', { 'enduser': enduser, 'emailgreeting': messagetohost, 
    	'useremail': useremail, 'firstname':firstname, 'lastname':lastname, 'ref_message': ref_message, })
    subject = "A New User Has Registered (Full User) - No Request to Connect"
    send_mail(subject, message, 'Blocbox User Registration <admin@blocbox.co>', ['admin@blocbox.co',]) 
    return HttpResponse("An email has been sent to admin@blocbox.co notifying the blocbox team of the new user.")


#send an email to the user that requested to connect
def requesthasbeensent(request, hostid, userid):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=userid)
    message = render_to_string('emails/requesthasbeensent.txt', {'host': host, 'enduser': enduser,})
    subject = "Your request to connect has been sent!"
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [enduser.email,])

def notifyconnectionconfirmed(request, hostid, userid):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=userid)
    message = render_to_string('emails/notifyconnectionconfirmed.txt', {'host': host, 'enduser': enduser,})
    subject = "Your request to connect was confirmed!"
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [enduser.email,])



#-----------------------------------------------------------
# Confirm or deny requests to connect
#-----------------------------------------------------------
#note that the url pattern is http://107.170.128.21/<host_id>/requestconnectconfirm/<user_id> -- defined in blocbox.urls
def confirmrequestconnect(request, host_id, user_id):
#url(r'^email/(?P<host_id>\d+)/requestconnectconfirm/(?P<user_id>\d+)/$', views.confirmrequestconnect, name='confirmrequestconnect'),
    host = get_object_or_404(UserInfo, pk=host_id)
    enduser = get_object_or_404(UserInfo, pk=user_id)
    neighborstatus, created = Connection.objects.get_or_create(host_user=host, end_user=enduser)
    neighborstatus.save() #update the Connections table to connect these user
    notifyconnectionconfirmed(request, host.id, enduser.id) #notify the enduser that the request was successful
    thank_you_message = enduser.first_name + "'s request to connect with you has been confirmed."
    return render(request, 'blocbox/thanks.html', { 'thank_you_message': thank_you_message, 'suggested_return_url': 'dashboard', 'suggested_return_message': "Return to your dashboard." })
    #return HttpResponse("The neighbor's request to connect has been confirmed.") 
    #update this to include host and enduser ids, e.g.: HttpResponse:looking at question %s." % question_id)

#waitlist almost finished and confirmation
def waitlist_almostfinished(request):
		return render(request, 'blocbox/almost-finished.html')
    

def joinwaitlist(request, referring_user_email=None, neighborhood=None):	
    neighborhood_text = None
    if neighborhood == 'clintonhill':
       neighborhood_text = "Clinton Hill"
    if neighborhood == 'brooklyn':
        neighborhood_text = "Brooklyn"
    if request.method == 'POST':  
    #if request.is_ajax():   	
        #formresponse = QueryDict(request.body)
        formresponse = json.loads(request.body)
        csrftoken = formresponse[0]
        email = formresponse[1]['value']      
        waitlistuser = Waitlist.objects.create(email=email)	
        waitlistuser.first_name = formresponse[2]['value']
        zipcodeform = formresponse[3]['value']
        waitlistuser.zipcode = zipcodeform
        waitlistuser.referredby = formresponse[4]['value']
        if len(formresponse) > 5:
            waitlistuser.hostinterest = formresponse[5]['value']
        else:
            waitlistuser.hostinterest = False
        zipcode = zcdb[zipcodeform]           
        zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 2)]
        zipcodes_nearby_json = json.dumps(zipcodes_nearby)
        waitlistuser.city = zipcode.city
        waitlistuser.state = zipcode.state
        waitlistuser.zipcodes_nearby = zipcodes_nearby_json
        waitlistuser.responseobject = formresponse
        waitlistuser.save()
        #add neighbors nearbyu
        add_neighbors_nearby_waitlist(waitlistid=waitlistuser.id)
        #Attribute the referral
        if referring_user_email:
            attribute_referral_waitlist(referring_user_email)
        #send_form_to_mailchimp(request, waitlistuser.id)
        message = "Success! You posted data to the user model"                  
    else:
        message = "The request method was not Ajax"
    return render(request, 'blocbox/joinwaitlist.html', { 
        'referring_user_email': referring_user_email, 'neighborhood': neighborhood, 'neighborhood_text': neighborhood_text  } )


def joinwaitlist_noajax(request):
    return render(request, 'blocbox/joinwaitlist_noajax.html')
 

def send_form_to_mailchimp(request, waitlistuserid):
    waitlistuser = Waitlist.objects.get(pk=waitlistuserid)
    url = 'http://blocbox.us8.list-manage.com/subscribe/post?u=a7a534bd9460b420e502241f0&amp;id=a442e04636'
    values = {'email': waitlistuser.email, 'first_name': waitlistuser.first_name, 'zipcode': waitlistuser.zipcode, 
    					'referredby': waitlistuser.referredby, 'hostinterest': waitlistuser.hostinterest, }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()
    message = "The email for thee waitlist user ID " + str(waitlistuser.id) + " is: " + waitlistuser.email
    return HttpResponse(message)

def joinwaitlist_testformpost(request, referring_user_email=None ):
    if request.method == 'POST':
    #if request.is_ajax():
        formresponse = json.loads(request.body)
        csrftoken = formresponse[0]
        email = formresponse[1]['value']      
        waitlistuser = Waitlist.objects.create(email=email)	
        waitlistuser.first_name = formresponse[2]['value']
        zipcodeform = formresponse[3]['value']
        waitlistuser.zipcode = zipcodeform
        waitlistuser.referredby = formresponse[4]['value']
        if len(formresponse) > 5:
            waitlistuser.hostinterest = formresponse[5]['value']
        else:
            waitlistuser.hostinterest = False
        zipcode = zcdb[zipcodeform]           
        zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 2)]
        zipcodes_nearby_json = json.dumps(zipcodes_nearby)
        waitlistuser.city = zipcode.city
        waitlistuser.state = zipcode.state
        waitlistuser.zipcodes_nearby = zipcodes_nearby_json
        waitlistuser.responseobject = formresponse
        waitlistuser.save()
        #add neighbors nearbyu
        add_neighbors_nearby_waitlist(waitlistid=waitlistuser.id)
        message = "Success! You posted data to the user model"                    
    else:
        message = "The request method was not Ajax"
    return render(request, 'blocbox/joinwaitlist_formtestpost.html', { 'referring_user_email': referring_user_email,    } )

     
def waitlist_confirmation(request):
		return render(request, 'blocbox/waitlist-confirmation.html')







#----------------------------------------------------------------
#OLD
#----------------------------------------------------------------
#Origial index, redefine as oldindex
def oldindex(request):
	    return HttpResponse("OldIndex - This was the first view for the blocbox module" + 
											"code is at django_project/django_project/bloc/views.py")

def searchold(request):
    return render(request, 'blocbox/old/search.shtml') 

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