from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.template import RequestContext, loader #allows it to load templates from blocbox/templates
from core.models import UserInfo, Transaction, Connection
#from django.contrib.auth.models import User #dont need this because not using User - maybe why it create table..
from core.forms import UserForm, HostForm
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


#Write a custom template filter:
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return render(request, 'blocbox/index.html') #loads blocbox/templates/blocbox/index.html 

def beta(request):
    return render(request, 'blocbox/beta.html') #load the blocbox/templates/blocbox/beta.html 



def search(request):
    return render(request, 'blocbox/search.html')

def searchold(request):
    return render(request, 'blocbox/old/search.shtml') 

def dashboard(request):
    return render(request, 'blocbox/dashboard.html')

def myblock(request):
    return render(request, 'blocbox/myblock.html')
        
#dashboard - old version passing args - dont think i need
"""
def dashboard(request, userinfo_id):
    context = RequestContext(request)
    user = get_object_or_404(UserInfo, pk=userinfo_id)
    return render_to_response('blocbox/dashboard.html', {'user':user}, context)
"""

#Create the view for the hostprofile
def hostprofile(request, userinfo_id):
    context = RequestContext(request)
    host = get_object_or_404(UserInfo, pk=userinfo_id)
    enduser = request.user
    if enduser.is_authenticated():
        connected = Connection.objects.are_neighbors(user1=enduser, user2=host) #true of false, but not sure how to call thee user...
    else:
        connected = False
    connections_all = Connection.objects.filter(host_user=host) 
    connections_count = Connection.objects.filter(host_user=host).count() #count them,removing status=0 after host_user=host   
    transactions_all = Transaction.objects.filter(payee=host)
    transactions_count = Transaction.objects.filter(payee=host).count() #count all of the transactions
    return render_to_response('blocbox/host-profile.html', {'host':host, 'enduser':enduser, 'connected':connected,
    		'connections_all':connections_all, 'connections_count':connections_count, 'connectionstotal':connections_count,
    		'transactions_count':transactions_count, 'transactions_all':transactions_all }, context)

#Create a login viewi
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
def signupconnect(request, userinfo_id):
    host = get_object_or_404(UserInfo, pk=userinfo_id)
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
 
#Origial index, redefine as oldindex
def oldindex(request):
	    return HttpResponse("OldIndex - This was the first view for the blocbox module" + 
											"code is at django_project/django_project/bloc/views.py")

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
def confirmrequestconnect(request, host_id, user_id):
#url(r'^email/(?P<host_id>\d+)/requestconnectconfirm/(?P<user_id>\d+)/$', views.confirmrequestconnect, name='confirmrequestconnect'),
    context = RequestContext(request)
    host = get_object_or_404(UserInfo, pk=host_id)
    enduser = get_object_or_404(UserInfo, pk=user_id)
    neighborstatus, created = Connection.objects.get_or_create(host_user=host, end_user=enduser)
    neighborstatus.save() #update the Connections table to connect these user
    notifyconnectionconfirmed(request, host.id, enduser.id) #notify the enduser that the request was successful
    return HttpResponse("The neighbor's request to connect has been confirmed.") 
    #update this to include host and enduser ids, e.g.: HttpResponse:looking at question %s." % question_id)

#waitlist almost finished and confirmation
def waitlist_almostfinished(request):
		return render(request, 'blocbox/almost-finished.html')

def waitlist_confirmation(request):
		return render(request, 'blocbox/waitlist-confirmation.html')


def startashipment(request):
		return render(request, 'blocbox/startashipment.html')
		
def payment(request):
		return render(request, 'blocbox/payment.html')

def shippackage(request):
		return render(request, 'blocbox/shippackage.html')
		




#------------------------------------------------------------------------------------
#Tests
#------------------------------------------------------------------------------------
#bootsrap test - copy of the waitlist sign-up page
def bootstraptest(request):
    return render(request, 'blocbox/x_bootstraptest.html') 

#style tests
def styletest(request):
    return render(request, 'blocbox/x_styletest.html') 
    
#jessstest - rendering calendar, note that claneder_slug is passed as argument in URL in base scheduling app
def jesstest(request, calendar_slug_single = "testcalendar1", host_id=2):
    enduser = request.user
    host = get_object_or_404(UserInfo, pk=host_id)
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
    calendar_single = get_object_or_404(Calendar, slug=calendar_slug_single) #this is working
    event_list_single = GET_EVENTS_FUNC(request, calendar_single)  #this is working 
    thismonth_object_single = Month(event_list_single, date, None, None, local_timezone) #specific to the calendar  
    #Show all calendars associated with a particular host, host_id is currently defined above when called - want to pass it in URL
    cal_relations_all = CalendarRelation.objects.all() #this is a list of CalendarRelation objects
    cal_relations_host = CalendarRelation.objects.filter(object_id=host.id)
    cal_relations_host_count = CalendarRelation.objects.filter(object_id=host.id).count()
    cal_list_host = []
    for cal in cal_relations_host:
        calhost = get_object_or_404(Calendar, id=cal.calendar_id)
        #calhost = Calendar.objects.filter(id=cal.calendar_id) #the problem is that this creates its own list...
        cal_list_host.append(calhost)
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