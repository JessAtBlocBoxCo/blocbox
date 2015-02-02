from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.template import RequestContext, loader #allows it to load templates from blocbox/templates
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
#Add CORE and TRANSACTIONS models
from core.models import UserInfo
from connections.models import Connection
from transactions.models import Transaction
#from django.contrib.auth.models import User #dont need this because not using User - maybe why it create table..
from core.forms import UserForm, HostForm
from connections.forms import ConnectForm
from transactions.forms import TrackingForm, ModifyTransaction, PackageReceived, EndUserIssue
#Important the authentication and login functions -- not sure that i can use with custom model
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
##Adding email functionality (http://catherinetenajeros.blogspot.com/2013/03/send-mail.html)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.list import ListView
#import scheduling stuff
import datetime
import pytz
from urllib import quote
#from schedule import periods
from schedule.periods import Month
from schedule.periods import weekday_names
from schedule.conf.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT
from schedule.forms import EventForm, OccurrenceForm
from schedule.models import Calendar, Occurrence, Event
from schedule.models.calendars import CalendarRelation
from schedule.utils import check_event_permissions, coerce_date_dict
from django.utils import timezone
#Import Payment Stuff
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.views import ask_for_money
#Import Messaging Stuff
from django.contrib import messages
from django_messages.models import Message
from django_messages.forms import ComposeForm
from django_messages.utils import format_quote, get_user_model, get_username_field
#aftership
import aftership
AFTERSHIP_API_KEY = settings.AFTERSHIP_API_KEY #DEFINED IN SETTINGS.PY


#Write a custom template filter:
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    

#-------------------------------------------------------------------------
#Waitlist, beta, getting started, about and dashboard/profile pages
#-------------------------------------------------------------------------
def waitlist(request):
    return render(request, 'blocbox/waitlist.html') #loads blocbox/templates/blocbox/waitlist.html 

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

def aboutblocbox(request):
    enduser = request.user
    return render(request, 'blocbox/aboutblocbox.html', {'enduser': enduser,})
    	
def abouthosting(request):
    enduser = request.user
    return render(request, 'blocbox/abouthosting.html', {'enduser':enduser,})

def dashboard(request, host_id=None, trans=None, track_id=None, confirm_id=None, issue_id=None, message_trans_id=None ): #modify_id=None
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None
    #Vars that do not depend on authentication
    api = aftership.APIv4(AFTERSHIP_API_KEY) #Defined in settings.py
    datetimenow = datetime.datetime.now()
    datetoday = datetime.date.today()
    shipments_with_tracking_allpaid = []                 
    shipments_with_tracking_complete = []                
    shipments_with_tracking_notcomplete = []             
    shipments_with_tracking_notcomplete_delivered = []   
    shipments_with_tracking_notcomplete_notdelivered = []
    shipments_with_tracking_notcomplete_notrackingno = []
    #variables requiring authentication
    if enduser.is_authenticated():
        connections_all = Connection.objects.filter(end_user=enduser) 
        connections_count = connections_all.count() #count them,removing status=0 after host_user=host
        #determine whether they are only connected to one host for pupose of 'start a shipment' link
        if connections_count==1:
            hostonly=connections_all[0].host_user
        else:
            hostonly=None 
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
    if track_id:  #if they open a tracking modal
        dashboard_tracking_modal(request, track_id) #defined below
    else: #if no track_id (if they dont open the modal)    
        tracking_form = None  
    if confirm_id:  #if the open the package_received modal
        package_received_modal(request, confirm_id)
    else: #if they dont open the packge received modal
    		package_received_form = None
    if issue_id:     #if they open the EndUser Issues Modal/Button
        enduser_report_issue_modal(request, issue_id)
    else:
        enduser_issue_form = None #if they dont open the report an issue modal
    if message_trans_id: #if they open the message host modal
        message_host_modal(request, message_trans_id)
    else: #if they dont open the message host modal
        compose_form = None  
    return render(request, 'blocbox/dashboard.html', {
        'enduser': enduser, 'host': host, 'datetimenow': datetimenow, 'datetoday': datetoday,
        'connections_all': connections_all, 'connections_count': connections_count,
        'hostonly': hostonly, 'request': request,  'trans': trans, 
        'track_id': track_id,
        'tracking_form': tracking_form, 'package_received_form': package_received_form, 'enduser_issue_form': enduser_issue_form, 'compose_form': compose_form, 
        #shipments lists
        'shipments_with_tracking_allpaid': shipments_with_tracking_allpaid, 'shipments_with_tracking_complete': shipments_with_tracking_complete, 
        'shipments_with_tracking_notcomplete': shipments_with_tracking_notcomplete, 
        'shipments_with_tracking_notcomplete_delivered': shipments_with_tracking_notcomplete_delivered, 'shipments_with_tracking_notcomplete_notdelivered': shipments_with_tracking_notcomplete_notdelivered,
        'shipments_with_tracking_notcomplete_notrackingno': shipments_with_tracking_notcomplete_notrackingno,
        #other favors lists
        'otherfavors_all_paid': otherfavors_all_paid, 
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

def dashboard_tracking_modal(request, track_id):
    trans = Transaction.objects.get(pk=track_id)  
    tracking_on_trans = str(trans.tracking)
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
                    if trans.enduser.first_name:
                        customer_name = str(trans.enduser.first_name) + " " + str(trans.enduser.last_name)
                    else:
                        customer_name = str(trans.enduser.email)   
                    #aftership error codes: https://www.aftership.com/docs/api/4/errors
                    #except aftership.APIv4RequestException as error:
                    #print 'Error:', error.code(), error.type(), error.message()
                    #see if its already on aftership
                    try:
                        api.trackings.post(tracking=dict(
    		                    slug=slug_detected, tracking_number=tracking_no_to_add,  
    		                    title=str(trans.title) + ": Order " + str(trans.id)+": User " + enduser.email+" to Host " + trans.host.email, 
    		                    order_id=str(trans.id),
    		                    customer_name=customer_name,
    		                    emails=[trans.enduser.email, trans.host.email], #Emails for notifications
    		                    custom_fields=dict(Host_Email=trans.host.email, Invoice=trans.invoice)
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
                    datadict_added = api.trackings.get(slug_detected, tracking_no_to_add)
                    trackingdict_added = datadict_added.get(u'tracking')
                    #Save this information to trans table
                    trans.on_aftership = True
                    trans.shipment_courier = slug_detected.upper()
                    trans.save()
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


def message_host_modal(request, message_trans_id):
    trans = Transaction.objects.get(pk=message_trans_id)
    if request.method == 'POST':
        compose_form = ComposeForm(request.POST, recipient_filter=None) #maybe update recipient filter so it goes to the host in question, or can just use trans.host.id
        sender = request.user
    		#Add recipient here?
        recipient = trans.host.email
        compose_form.fields['recipient'].initial = recipient
        if compose_form.is_valid():
            compose_form.save(sender=request.user)
        else:
            print compose_form.errors
    else:
        compose_form = ComposeForm(recipient_filter=None)
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
    		else:
    				print package_received_form.errors
    else:
    	  package_received_form = PackageReceived()
    return HttpResponse("OK")


#END DASHBOARD DEFS
    
def myblock(request):
    return render(request, 'blocbox/myblock.html')
        
def profile(request):
    enduser = request.user
    return render(request, 'blocbox/profile.html', {'enduser':enduser,})
    
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
                return HttpResponseRedirect('/dashboard/') #update in future to go to beta, with user credentials
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your BlocBox account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(email, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('blocbox/sign-in.html', {}, context)

#logout function
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/beta/')

#Registration Form -- User 
def signupconnect(request, host_id):
    host = get_object_or_404(UserInfo, pk=host_id)
    context = RequestContext(request)
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
            # Now we hash the password with the set_passworth method
            # Once hashed, we ca update the user object
            user.set_password(user.password)
            user.save()   	      
            #FILL THIS IN LATER - NEED TO INSTALL THE PIL THING AND ADD A PICTURE FIELD
            #if 'picture' in request.FILES:
            #profile.picture = request.FILES['picture']       	      
            registered = True #Update our variable to tell the template registration was successful        
            #send an email to the host askig them to confirm the connection
            confirmconnect_mail(request, host.id, user.id, user.intro_message, user.email, user.first_name, user.last_name) #send a request to connect to the host
            #send a email to the enduser/ person requesting to connect thakign them for registering and telling them the request was sent
            requesthasbeensent(request, host.id, user.id)
    	  #Invalid form or forms - print problems to the terminal so they're show to user
    	  else: 
    	      print user_form.errors
    	  
    #If Not a HTTP POST, so we render our form using ModelForm instances - these forms will be blank, ready for user input
    else:
        user_form = UserForm()
    	  
    #Render the template depending on the context
    #the template is here: /home/django/blocbox/core/templates/blocbox/blocbox.html
    return render_to_response(
            'blocbox/sign-up-connect.html', #formerly registeruser.html
    	      {'user_form': user_form, 'registered': registered, 'host':host },
    	      context)
   	#PASS ARGUMENTS
		#return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		
#Registration Form -- User
def signupnoconnect(request):
    context = RequestContext(request)
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
    	      # Now we hash the password with the set_passworth method
    	      # Once hashed, we ca update the user object
    	      user.set_password(user.password)
    	      user.save()
    	      
    	      #FILL THIS IN LATER - NEED TO INSTALL THE PIL THING AND ADD A PICTURE FIELD
    	      #if 'picture' in request.FILES:
    	      #    profile.picture = request.FILES['picture']
    	         	      
    	      registered = True #Update our variable to tell the template registration was successful
    	  		
    	  #Invalid form or forms - print problems to the terminal so they're show to user
    	  else: 
    	      print user_form.errors
    	  
    #If Not a HTTP POST, so we render our form using ModelForm instances - these forms will be blank, ready for user input
    else:
        user_form = UserForm()
  
    return render_to_response(
            'blocbox/sign-up-withoutconnect.html', 
    	      {'user_form': user_form, 'registered': registered},
    	      context)


#Registration Form - Host
#FIGURE OUT - DOES THE HOST NEED TO BE REGISTERED AS UER FIRST? CAN WE IMPORT AL THAT
#signuphost url is www.blocbox.co/signuphost
def signuphost(request):
    context = RequestContext(request)
    registered = False 
    if request.method == 'POST':
        host_form = HostForm(data=request.POST)
        if host_form.is_valid():
            host = host_form.save() #save the hosts form data to the database
        
            #dont need this if the hos tinfo includes all of the user info
            #FILL THIS IN LATER - NEED TO INSTALL THE PIL THING AND ADD A PICTURE FIELD
    	      #if 'picture' in request.FILES:
    	      #    profile.picture = request.FILES['picture']
    	      #host.user = user #same.. what does this do?.. not sure we need it
            host.save() #Save the HostProfile model instance
            registered = True   	  
    	          
    	  #Invalid form or forms - print problems to the terminal so they're show to user
        else: 
    	      print host_form.errors
    
    #Not a HTTP Post, so render our form using tow ModelForm instances, will be blank, reader for use rinput   
    else:
        host_form = HostForm()

    return render_to_response(
            'blocbox/sign-up-host.html',
    	      {'host_form': host_form, 'registered': registered},
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
#return render_to_response(
# 'blocbox/sign-up-connect.html', {'user_form': user_form, 'registered': registered, 'host':host },context)

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

def waitlist_confirmation(request):
		return render(request, 'blocbox/waitlist-confirmation.html')








#--------------------------------------------------------------
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