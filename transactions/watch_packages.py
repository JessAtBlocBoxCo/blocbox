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
trans_aftership_notarchived = transactions_onaftership.exclude(trans_archived=True)

def main():
    response_messages_list = []
    for trans in trans_aftership_notarchived:
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
        #update time updated, its formatted like this in api: 'last_updated_at': u'2015-03-10T16:43:41+00:00'
        last_tracking_unicode = tracking_info['last_updated_at']
        last_tracking_datetime = datetime.datetime.strptime(last_tracking_unicode, '%Y-%m-%dT%H:%M:%S+00:00')
        trans.last_tracking_datetime = last_tracking_datetime
        trans.last_tracking_date = last_tracking_datetime.date()
        trans.save()
        if new_status == 'Expired':
            if trans.aftership_expired == False:
                trans.aftership_expired = True
                trans.save()
            if trans.on_aftership == True:
                trans.on_aftership = False
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
            last_tracking_datetime = None
        responsemessage = "The last tracking dateitme was " + str(last_tracking_datetime) + "."
        response_messages_list.append(responsemessage)
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
            if status_change == True:
                trans.last_tracking_status = new_status
                trans.save()
                #send mail
                #notify_enduser_tracking_change(request, host.id, enduser.id, trans.id)
                #if its expired dont do anythin
                tracking_link = "https://blocbox.aftership.com/" + str(trans.tracking)
                if trans.title:
                    trans_title = "(" + trans.title + ")"
                else:
                    trans_title = None
                if host.st_address2:
                    host_address_full = host.st_address1 + ", " + host.st_address2
                else:
                    host_address_full = host.st_address1
                sendit = False
                if new_status == 'Expired':
                    responsemessage = "Transaction ID " + str(trans.id) + " has expired" + "\n"  
                    trans.aftership_expired = True
                    trans.on_aftership = False
                    trans.save()              
                elif new_status == 'Delivered':
                    if enduser.notifyuser_packagereceived == True:
                	      sendit = True
                    subject = "Your Package Has Been Delivered to the Host"  
                    message_body = "Your package, transaction ID " + str(trans.id) + " " + trans_title + " has been delivered to your host, " + host.first_name + host.last_name + ", at " + host_address_full + "!"                  
                    responsemessage ="An email has been sent to " + str(enduser.email) + " notifying them that trans id " + str(trans.id) + " was delivered" + "\n"
                elif new_status == 'Exception':
                    if enduser.notifyuser_deliveryexception == True:
                	      sendit = True
                    subject = "There was a delivery exception for transaction ID " + str(trans.id)
                    message_body = "There was a delivery exception for your package, transaction ID " + str(trans.id) + " " + trans_title + "."
                    responsemessage = "An email was sent to " + str(enduser.email) + " notifying them that trans ID " + str(trans.id) + " had a delivery exception" + "\n"
                elif new_status == 'InTransit':
                    if enduser.notifyuser_packageships == True:
                	      sendit = True
                    message_body = "Your package, transaction ID " + str(trans.id) + " " + trans_title + " is in transit!"
                    subject = "Your Package is in Transit"
                    responsemessage = "Package for " + str(enduser.email) + " trans ID " + str(trans.id) + " is in transit. email sent? " + str(sendit)
                else:
                    message_body = "There was a tracking update for your package, transaction ID " + str(trans.id) + " " + trans_title + ".  The status was changed from " + current_status + " to: " + new_status + "."
                    subject = "The tracking information for your package has been updated"
                    responsemessage = "Tracking info for trans ID " + str(trans.id) + " has been updated to " + new_status + " no email sent" + "\n"
                message = render_to_string('emails/notify_enduser_trackingupdate.txt', { 'host': host, 'enduser': enduser, 'trans': trans,
                		'new_status': new_status, 'message_body': message_body, 'tracking_link': tracking_link, })
                if sendit == True:
                    send_mail(subject, message, 'Blocbox Tracking <admin@blocbox.co>', [enduser.email,])    
                response_messages_list.append(responsemessage)
            else:
                responsemessage = "The status did not change for trans id " + str(trans.id) + "; the status is: " + new_status + "\n"
                response_messages_list.append(responsemessage)   
    #return HttpResponse(response_messages_list)
    #the httpResponse produces a formatted output when called from command line but not from python shell.. when i sort this out go back to hhptResponse
    return response_messages_list

def test_celery_beat(enduserid, hostid, transid):
    trans = Transaction.objects.get(pk=transid)
    enduser = UserInfo.objects.get(pk=enduserid)
    host = UserInfo.objects.get(pk=hostid)
    message_body = "this is a test of celery beat - send every 30 minues if the user has delivery notifications on"
    subject = "Testing scheduled celery tasks"
    message = render_to_string('emails/notify_enduser_trackingupdate.txt', { 'host': host, 'enduser': enduser, 'trans': trans,'message_body': message_body, })
    if enduser.notifyuser_packagereceived == True:
        send_mail(subject, message, 'Blocbox Tracking <admin@blocbox.co>', [enduser.email,])
        returnmessage = "An email was sent to test the celery beat -t he user has delivery notifications on"
    else:
        returnmessage = "The user does not appear to have delivery received notifications on"
    return returnmessage
        
       


if __name__ == "__main__":
    sys.exit(main())