#This is blocbox.transactions.views.py
from django.shortcuts import render
import datetime
import random
import pytz
from urllib import quote
from django.views.decorators.csrf import csrf_exempt
#from django
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
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
#from paypal.standard.ipn import views
#import new homebrew calendar jazz
from calendar_homebrew.models import HostConflicts, HostWeeklyDefaultSchedule
from calendar_homebrew.forms import CalendarCheckBoxes
import calendar 
calendar.setfirstweekday(6) #Set first weekday: 6 is sunday, 0 is monday, default is 0/monday
#import transaction models
from transactions.models import Transaction
from transactions.forms import CreatePackageTransaction
##Adding email functionality (http://catherinetenajeros.blogspot.com/2013/03/send-mail.html)
from django.core.mail import send_mail
from django.template.loader import render_to_string

#The Start a shipment process
def startashipment(request, host_id=None, transaction_form_submitted=False, invoice=None, cal_form_submitted=False, packagedays_count = None, ):
    random3digits = random.randint(100,999)
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
        host = None  
    #Determine if payment is needed or balance will suffice
    package_price = host.price_package_per
    balance = enduser.account_balance
    if balance >= package_price:
        payment_needed = False
        amount_due = 0.00
        remaining_balance = balance - package_price
    else:
        payment_needed = True
        amount_due = None #this is processed on the payment page if they aren't applying account balance
        remaining_balance = None 
    connections_all = Connection.objects.filter(end_user=enduser) 
    #Get date fields
    local_timezone = request.session.setdefault('django_timezone', 'UTC')
    local_timezone = pytz.timezone(local_timezone) 
    date_today = datetime.date.today()
    datetime_now = datetime.datetime.now()         
    time = datetime.datetime.time(datetime_now)
    #Year variables
    thisyear = date_today.year
    nextyear = date_today.year + 1
    thisyear_isleap = calendar.isleap(thisyear)
    nextyear_isleap = calendar.isleap(nextyear)
    #Month Variables
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
    today_dayofmonth_num = date_today.day 
    #Empty variables for availability/ conflict stuff
    days_package_may_come_thismonth = []
    days_package_may_come_nextmonth = []
    month1days_count = None
    month2days_count = None
    conflicts_date_from = []
    conflicts_startmonths = []
    conflicts_startthismonth = []
    conflicts_startnextmonth = []
    conflicts_startandend_thismonth = []
    conflicts_startandend_nextmonth = []
    conflicts_startthismonth_endnextmonth = []
    conflicts_startthismonth_endlater = []
    conflicts_startnextmonth_endlater = []
    days_withconflicts_thismonth = []
    days_withconflicts_nextmonth = []
    days_withconflicts_later = []
    #if host/no host - get caklendar_homebrew created fields
    if host:
        transcount = Transaction.objects.filter(host=host).count() + 1 #counts transactions that this receiver_email has received (could change to host email)
        invoice = "H" + str(host.id) + "U" + str(enduser.id) + "N" +str(transcount) +"D" + str(date_today.month) + str(date_today.day) + str(time.hour) + "R" + str(random3digits) #h2u14N13D112210R123 = transaciton between host2, user14, host's 13th transaction
        conflicts = HostConflicts.objects.filter(host=host)
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
            days_withconflicts_nextmonth.append(conflict.date_from.day)   
            #append the days after the first day for multi-day conflicts 	  
            if conflict.duration > 1:
                duration_less1 = conflict.duration - 1
                for day in range(duration_less1):
                    conflict_day = conflict.date_from.day + day + 1 #range starts at zero so have to add 1
                    if conflict_day <= days_in_nextmonth:
                        days_withconflicts_nextmonth.append(conflict_day)
                    else:
                        conflict_day_spillover = conflict_day - days_in_nextmonth
                        days_withconflicts_later.append(conflict_day_spillover)
        #remove duplciates - hopefully they dont exist but the might          
        days_withconflicts_thismonth = list(set(days_withconflicts_thismonth))
        days_withconflicts_nextmonth = list(set(days_withconflicts_nextmonth))
        #determine if there is a conflict
        host_package_conflict = False
        for day in days_package_may_come_thismonth:
            if day in days_withconflicts_thismonth:
                host_package_conflict = True
        for day in days_package_may_come_nextmonth:
            if day in days_withconflicts_nextmonth:
                host_package_conflict = True
    else: #if no host specified that stuff is empty/none
        conflicts = None	
        host_package_conflict = False  
    #do payment variables/ transaction form stuff once they've checked the calendar day
    favortype='package'
    #transaction_form_submitted = False
    packagedays_count = None
    cal_form_submitted = False
    if cal_form_submitted == False:     
        trans_form_package = None 
        packagedays = []  
        packagedays_string = []
        if request.method == 'POST':
            cal_form = CalendarCheckBoxes(data=request.POST)
            if cal_form.is_valid():  
                for daynumber in range(1,32):  #starts at zero otherwise so this will stop at 31   	     
                    daycheckedmonth1 = cal_form.cleaned_data['month1day'+str(daynumber)]    
                    if daycheckedmonth1:
                    	  #checked day needs to be in YYYY-MM-DD  format
                        checked_day = str(thisyear) + "-" + str(thismonth_num) + "-" + str(daynumber)
                        checked_day_string = str(thismonth) + " " + str(daynumber)
                        packagedays.append(checked_day)
                        packagedays_string.append(checked_day_string)
                        days_package_may_come_thismonth.append(daynumber)
                for daynumber in range(1,32): 
                    daycheckedmonth2 = cal_form.cleaned_data['month2day'+str(daynumber)] 
                    if daycheckedmonth2:
                        checked_day = str(thisyear) + "-" + str(nextmonth_num) + "-" + str(daynumber) 
                        checked_day_string = str(nextmonth) + " " + str(daynumber)
                        packagedays.append(checked_day)
                        packagedays_string.append(checked_day_string)
                        days_package_may_come_nextmonth.append(daynumber)                                   
                month1days_count = len(days_package_may_come_thismonth)
                month2days_count = len(days_package_may_come_nextmonth)
                cal_form_submitted = True
            else:
                print cal_form.errors
        else:
            cal_form = CalendarCheckBoxes()     
        packagedays_count = len(packagedays) 
    trans_form_submitted = False
    if cal_form_submitted == True:
        trans = Transaction()
        if request.method == 'POST': 
            trans_form_package = CreatePackageTransaction(request.POST)            
            if trans_form_package.is_valid():
                title = trans_form_package.cleaned_data['title']
                payment_option = trans_form_package.cleaned_data['payment_option']
                note_to_host = trans_form_package.cleaned_data['note_to_host']
                paypal_quantity = 1
                if payment_option=="bundle10":
                    price=15
                    youselected="Bundle of 10 Packages"  
                    balance_created = price - 2                  
                elif payment_option=="month20":
                    price=15
                    youselected="Monthly"       
                    balance_created = price - 2             
                elif payment_option=="annual":
                    price=150
                    youselected="Annual"
                    balance_created = price - 2
                else:
                    price=2
                    youselected="Per Package"
                    balance_created = None
                #Next, add the data to the transaction table
                trans.balance_created = balance_created
                trans.payment_option = payment_option
                trans.title = title
                trans.favortype = favortype
                trans.note_to_host = note_to_host
                trans.price = price
                trans.youselected = youselected
                trans.paypal_quantity = paypal_quantity
                trans.host = host
                trans.enduser = enduser
                trans.invoice = invoice
                #Account balance/ create amount_due
                if enduser.account_balance:
                    if enduser.account_balance >= price:
                        trans.amount_due = 0
                        trans.payment_needed = False
                    else:
                        trans.amount_due = price - enduser.account_balance
                        trans.payment_needed
                else:
                    trans.amount_due = price
                    trans.payment_needed = True
                arrivalwindow_days_count = trans_form_package.cleaned_data['packagedays_count']
                trans.arrivalwindow_days_count = arrivalwindow_days_count
                day1 = trans_form_package.cleaned_data['arrivalwindow_day1']
                day1string = trans_form_package.cleaned_data['arrivalwindow_day1string']
                if day1:
                    trans.arrivalwindow_day1 = day1
                day2 = trans_form_package.cleaned_data['arrivalwindow_day2']
                day2string = trans_form_package.cleaned_data['arrivalwindow_day2string']
                if day2:   
                    trans.arrivalwindow_day2 = day2
                day3 = trans_form_package.cleaned_data['arrivalwindow_day3']
                day3string = trans_form_package.cleaned_data['arrivalwindow_day3string']
                if day3:
                    trans.arrivalwindow_day3 = day3
                day4 = trans_form_package.cleaned_data['arrivalwindow_day4']
                day4string = trans_form_package.cleaned_data['arrivalwindow_day4string']
                if day4:
                    trans.arrivalwindow_day4 = day4
                day5 = trans_form_package.cleaned_data['arrivalwindow_day5']
                day5string = trans_form_package.cleaned_data['arrivalwindow_day5string']
                if day5:
                    trans.arrivalwindow_day5 = day5
                day6 = trans_form_package.cleaned_data['arrivalwindow_day6']
                day6string = trans_form_package.cleaned_data['arrivalwindow_day6string']
                if day6:
                    trans.arrivalwindow_day6 = day6
                day7 = trans_form_package.cleaned_data['arrivalwindow_day7'] 
                day7string = trans_form_package.cleaned_data['arrivalwindow_day7string'] 
                if day7:
                    trans.arrivalwindow_day7 = day7      
                if arrivalwindow_days_count == 1:
                    trans.arrivalwindow_string = str(day1string)
                    trans.arrivalwindow_lastday = day1
                if arrivalwindow_days_count == 2:
                    trans.arrivalwindow_string = str(day1string) + ", or" + str(day2string)
                    trans.arrivalwindow_lastday = day2
                if arrivalwindow_days_count == 3:
                    trans.arrivalwindow_string = str(day1string) + ", " + str(day2string) + ", or" + str(day3string)
                    trans.arrivalwindow_lastday = day3
                if arrivalwindow_days_count == 4:
                    trans.arrivalwindow_string = str(day1string) + ", " + str(day2string) + ", " + str(day3string) + ", or " + str(day4string)
                    trans.arrivalwindow_lastday = day4
                if arrivalwindow_days_count == 5:
                    trans.arrivalwindow_string = str(day1string) + ", " + str(day2string) + ", " + str(day3string) + ", " + str(day4string) + ", or" + str(day5string)
                    trans.arrivalwindow_lastday = day5
                if arrivalwindow_days_count == 6:
                    trans.arrivalwindow_string = str(day1string) + ", " + str(day2string) + ", " + str(day3string) + ", " + str(day4string) + ", " + str(day5string) + ", or" + str(day6string)
                    trans.arrivalwindow_lastday = day6
                if arrivalwindow_days_count == 7:
                    trans.arrivalwindow_lastday = day7
                    trans.arrivalwindow_string = str(day1string) + ", " + str(day2string) + ", " + str(day3string) + ", " + str(day4string) + ", " + str(day5string) + ", " + str(day6string) + ", or" + str(day7string)               
                trans.save() 
                transaction_form_submitted = True
            else:
                print trans_form_package.errors 
        else: 
            trans_form_package = CreatePackageTransaction()
    #if the transaction form has been submitted redirect to new page
    if transaction_form_submitted == True:
        cal_form = None 
        if payment_needed:
            return HttpResponseRedirect("/transactions/payment/host" + str(host.id) + "/invoice" + str(invoice) + "/favortype" + str(favortype) + "/") 
        else:
            return HttpResponseRediret("/transaction/shippackage/host" +string(host.id) + "/account_balance/invoice/" + str(invoice) + "/")
    #if the transaction form has not been submitted  
    else:   	   
        return render(request, 'blocbox/startashipment.html', {
		        'enduser':enduser, 'host': host, 'connections_all': connections_all, 
        	  #'cal_relations_host_count': cal_relations_host_count, 'cal_relations_host': cal_relations_host, 'cal_list_host': cal_list_host,
        	  'here': quote(request.get_full_path()),
        	  #Python calendar variables (independent of conflict app)
            'local_timezone': local_timezone, 'date_today': date_today, 'datetime_now': datetime_now,  
            'thisyear': thisyear, 'nextyear': nextyear, 'thisyeaer_isleap': thisyear_isleap, 'nextyear_isleap': nextyear_isleap,
            'thismonth': thismonth,  'nextmonth': nextmonth, 'thismonth_calendar': thismonth_calendar, 'nextmonth_calendar': nextmonth_calendar,
            'monthrange_thismonth': monthrange_thismonth, 'monthrange_nextmonth': monthrange_nextmonth, 'days_in_thismonth': days_in_thismonth, 'days_in_nextmonth': days_in_nextmonth, 
            'today_dayofmonth_num': today_dayofmonth_num, 'nextmonth_calendar_year': nextmonth_calendar_year,
            #conflict app variables (if host)
        	  'conflicts': conflicts, 'conflicts_startthismonth': conflicts_startthismonth, 'conflicts_startnextmonth': conflicts_startnextmonth, 
        	  'conflicts_startandend_thismonth': conflicts_startandend_thismonth, 'conflicts_startandend_nextmonth': conflicts_startandend_nextmonth,
        	  'days_withconflicts_thismonth': days_withconflicts_thismonth, 'days_withconflicts_nextmonth': days_withconflicts_nextmonth,       
        	  #days package may come
        	  'days_package_may_come_thismonth': days_package_may_come_thismonth, 'days_package_may_come_nextmonth': days_package_may_come_nextmonth,
        	  'host_package_conflict': host_package_conflict,
        	  #Calendar check boxes form
        	  'cal_form': cal_form,  'packagedays': packagedays, 'packagedays_string': packagedays_string, 'packagedays_count': packagedays_count, 'cal_form_submitted': cal_form_submitted,
        	  #payment stuff once the calendar checkboxes are checked
        	  'trans_form_package': trans_form_package, 'invoice': invoice, 'favortype': favortype, 'transaction_form_submitted': transaction_form_submitted, 'random3digits': random3digits,
		    		'payment_needed': payment_needed, 'amount_due': amount_due, 'remaining_balance': remaining_balance,
		    })



 

#starat a shipmetn view if requested from navbar
def nav_startashipment(request, host=None):
    enduser = request.user
    connections_all = Connection.objects.filter(end_user=enduser) 
    connections_count = connections_all.count() #count them,removing status=0 after host_user=host
    if connections_count==1:
        host=connections_all[0].host_user
        templatename =  "blocbox/startashipment.html"
    if connections_count==0:
        templatename = "blocbox/search.html"
    else:
        templatename =  "blocbox/startashipment.html"
    return render(request, templatename, {
        'enduser': enduser, 'host': host, 'connections_all': connections_all, 'connections_count': connections_count,})





#START A FAVOR  
def startafavor(request, host_id=None):
		enduser = request.user
		return render(request, 'blocbox/startafavor.html', {'enduser':enduser,})

#starat a shipmetn view if requested from navbar
def nav_startafavor(request, host=None):
    enduser = request.user
    connections_all = Connection.objects.filter(end_user=enduser) 
    connections_count = connections_all.count() #count them,removing status=0 after host_user=host
    if connections_count==1:
        host=connections_all[0].host_user
        templatename =  "blocbox/startafavor.html"
    if connections_count==0:
        templatename = "blocbox/search.html"
    else:
        templatename =  "blocbox/startafavor.html"
    return render(request, templatename, {
        'enduser': enduser, 'host': host, 'connections_all': connections_all, 'connections_count': connections_count,})
    			
#This is the REturn URL for paypal IPN so  eeds to be CSRF exempt
@csrf_exempt		
def shippackage(request, host_id): #passes the host_id argument in URL
    #context = RequestContext(request)
    enduser = request.user
    if host_id:
        host = get_object_or_404(UserInfo, pk=host_id)
    else:
    	  host = None
    return render(request, 'blocbox/shippackage.html', {'enduser':enduser, 'host':host,} )

def shippackage_accountbalance(request, host_id, invoice):
    enduser = request.user
    host = get_object_or_404(UserInfo, pk=host_id)
    trans = Transaction.objects.get(invoice=invoice)
    userinfo = UserInfo.objects.get(pk=enduser.id) 
    new_account_balance = enduser.account_balance - trans.price 
    #update transaction table
    trans.payment_processed = True
    trans.payment_method = "Balance"
    trans.account_balance_before = enduser.account_balance
    trans.account_balance_after = new_account_balance
    trans.save()
    #update user info to subtract that amount from their balance
    userinfo.account_balance = new_account_balance
    userinfo.save()
    notify_host_shipment_paid(request,trans_id)
    notify_enduser_shipment_paid(request, trans_id) 
    return render(request, 'blocbox/shippackage.html', {'enduser':enduser, 'host':host, 'trans': trans})

#paypal_ipn views at blocbox/paypal/standard/ipn/views.py


def notify_host_shipment_paid(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    if trans.arrivalwindow_days_count == 1:
        arrivalwindow_estimate = 'on '+ str(trans.sarrivalwindow_string)
    else:
    	  arrivalwindow_estimate = 'on one of the following ' + str(trans.arrivalwindow_days_count) + ' days: ' + trans.arrivalwindow_string
    message = render_to_string('emails/notify_host_shipment_paid.txt', { 
        'host': host, 'enduser': enduser, 'note_to_host': trans.note_to_host, 
        'payment_option': trans.youselected, 'price': trans.price, 'arrivalwindow_estimate': arrivalwindow_estimate
        })
    subject = "Your Neighbor " + str(enduser.first_name) + " is sending your a package"
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [host.email,]) #last is the to-email
    return HttpResponse("A Shipment is coming to you.")
    
def notify_enduser_shipment_paid(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    host = trans.host
    enduser = trans.enduser
    if trans.arrivalwindow_days_count == 1:
        arrivalwindow_estimate = 'on '+ str(trans.sarrivalwindow_string)
    else:
    	  arrivalwindow_estimate = 'on one of the following ' + str(trans.arrivalwindow_days_count) + ' days: ' + trans.arrivalwindow_string
    message = render_to_string('emails/notify_enduser_shipment_paid.txt', { 
        'host': host, 'enduser': enduser, 'note_to_host': trans.note_to_host, 
        'useremail': enduser.email, 'firstname':enduser.first_name, 'lastname':enduser.last_name,
        'payment_option': trans.youselected, 'price': trans.price, 'arrivalwindow_estimate': arrivalwindow_estimate
        })
    subject = "Confirmed: You're sending a package to " + str(host.first_name)
    send_mail(subject, message, 'The BlocBox Team <admin@blocbox.co>', [enduser.email,]) #last is the to-email
    return HttpResponse("You're sending a package.") 