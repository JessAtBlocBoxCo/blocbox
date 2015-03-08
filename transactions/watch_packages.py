import os
import sys
from django.conf import settings
path = '/home/django/blocbox'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blocbox.settings")
#settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,TEMPLATE_DIRS=('/yourprojet/templates',))
from django.core.management import execute_from_command_line
import datetime
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.template import RequestContext, loader #allows it to load templates from blocbox/template
from django.views.generic.list import ListView
from django.utils import timezone
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

def main():
    response_messages_list = []
    for trans in transactions_onaftership:
        slug = str(trans.shipment_courier.lower())
        tracking = trans.tracking
        host = trans.host
        enduser = trans.enduser
        if trans.last_tracking_status:
            current_status = trans.last_tracking_status
        else:
            current_status = None
        #get the trackig status from aftership        
        datadict = api.trackings.get(slug, tracking)
        tracking_info = datadict.get(u'tracking') 
        new_status = tracking_info['tag']
        #if there wasn't a status, add it
        if current_status == None:
            trans.last_tracking_status = new_status
            trans.save()
            responsemessage = "Tracking status was added for trans id" + str(trans.id) + ", it was previously empty"
            response_messages_list.append(responsemessage)
        #if there was a current status, see if its different
        else:
            if new_status == current_status:
                status_change = False
            else:
                status_change = True
            #if status change is true then upate status and send a notificaton to the user
            if status_change == False:
                trans.last_tracking_status = new_status
                trans.save()
                #send mail
                #notify_enduser_tracking_change(request, host.id, enduser.id, trans.id)
                message = render_to_string('emails/notify_enduser_trackingupdate.txt', { 'host': host, 'enduser': enduser, 'trans': trans,
                		'new_status': new_status})
                #if its expired dont do anything
                if new_status == 'Expired':
                    responsemessage = "Transaction ID " + str(trans.id) + " has expired"
                elif new_status == 'Delivered':
                    subject = "Your Package Has Been Delivered to the Host"                    
                    responsemessage ="An email has been sent to the user notifying them that trans id " + str(trans.id) + " was delivered"
                elif new_status == 'Exception':
                    subject = "There was a delivery exception for transaction ID " + str(trans.id)
                    responsemessage = "An email was sent to the user notifying them that trans ID " + str(trans.id) + " had a delivery exception"
                elif new_status == 'InTransit':
                    subject = "Your Package is in Transit"
                    responsemessage = "An email was sent to the user notifying them that trans ID " + str(trans.id) + " is in transit"
                else:
                    subject = "The tracking information for your package has been updated"
                    responsemessage = "Tracking info for trans ID " + str(trans.id) + " has been updated to " + new_status + " an email was sent"
                send_mail(subject, message, 'Blocbox Tracking <admin@blocbox.co>', [enduser.email,])    
                response_messages_list.append(responsemessage)
            else:
                responsemessage = "The status did not change for trans id " + str(trans.id) + "; the status is: " + new_status + "\n"
                response_messages_list.append(responsemessage)
    return HttpResponse(response_messages_list)

#using .txt file and passing value(s)    
def notify_enduser_tracking_change(request, hostid, enduserid, transid):
    host = get_object_or_404(UserInfo, pk=hostid)
    enduser = get_object_or_404(UserInfo, pk=enduserid)
    trans = get_object_or_404(Transaction, pk=transid)
    message = render_to_string('emails/notify_enduser_trackingupdate.txt', { 'host': host, 'enduser': enduser, 'trans': trans})
    subject = "Your tracking information has been updated"
    send_mail(subject, message, 'Blocbox Tracking <admin@blocbox.co>', [enduser.email,])
    return HttpResponse("An email has been sent to the user notifying them that the tracking information was updated")
            


if __name__ == "__main__":
    sys.exit(main())