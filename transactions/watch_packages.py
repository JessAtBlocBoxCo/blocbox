import datetime
import pytz
from urllib import quote
from django.views.decorators.csrf import csrf_exempt
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
from transactions.models import Transaction
##Adding email functionality (http://catherinetenajeros.blogspot.com/2013/03/send-mail.html)
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

#GET A LIST OF ALL TRANSACTIONS ON AFTERHIP
transactions_onaftership = Transaction.objects.filter(on_aftership=True)

def watch_packages():
    for trans in transactions_onaftership:
        slug = trans.shipment_courier
        tracking = trans.tracking
        host = trans.host
        enduser = trans.enduser
        if trans.last_tracking_status:
            current_status = trans.last_tracking_status
        else:
            current_status = None
        #get the trackig status from aftership        
        datadict = api.trackings.get(slug, tracking)
        new_status = datadict['tag']
        #if there wasn't a status, add it
        if current_status == None:
            trans.last_tracking_status = current_status
        #if there was a current status, see if its different
        else:
            if new_status == current_status:
                status_change = False
            else:
                status_change = True
            #if status change is true then upate status and send a notificaton to the user
            if status_change = True:
            trans.last_tracking_status = new_status
            trans.save()
            #send mail
            notify_enduser_tracking_change(host.id, enduser.id, trans.id):
    return HttpResponse("OK")

#using .txt file and passing value(s)    
def notify_enduser_tracking_change(request, hostid, enduserid, transid):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=enduserid)
    trans = get_object_or_404(Transaction, pk=transid):
    message = render_to_string('emails/notify_enduser_trackingupdate.txt', { 'host': host, 'enduser': enduser, 'trans': trans}
    subject = "Your tracking information has been updated"
    send_mail(subject, message, 'Blocbox Tracking <admin@blocbox.co>', [enduser.email,])
    return HttpResponse("An email has been sent to the user notifying them that the tracking information was updated")
            
	