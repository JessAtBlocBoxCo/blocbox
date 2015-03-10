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
#pyzipcode
import pyzipcode
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

#GET A LIST OF ALL TRANSACTIONS ON AFTERHIP
transactions_onaftership = Transaction.objects.filter(on_aftership=True)


def get_zipcodes_nearby(userid, mileradius):
    enduser = UserInfo.objects.get(pk=userid)
    responsemessage = None
    zip = enduser.zipcode
    zipcode = zcdb[zip]
    zipnearby_string = enduser.zipcodes_nearby
    if zipnearby_string:
        responsemessage = "The zipcode_nearby string is on the User Table for " + str(enduser.email) + ". The zipcodes nearby string is " + str(enduser.zipcodes_nearby) + "."
    else:
        responsemessage = "The zipcode_nearby string is empty on the User Table for " + str(enduser.email) + "." 
    zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, mileradius)]
    responsemessage = responsemessage + " The zipcodes in a " + str(mileradius) + " mile radius of " + str(enduser.email) + " are: " + str(zipcodes_nearby) + "."
    return responsemessage

def add_zipcodes_nearby(userid, mileradius):
    enduser = UserInfo.objects.get(pk=userid)
    responsemessage = None
    zip = enduser.zipcode
    zipcode = zcdb[zip]
    zipnearby_string = enduser.zipcodes_nearby
    zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, mileradius)]
    if zipnearby_string:
        responsemessage = "The zipcode_nearby string is on the User Table for " + str(enduser.email) + ". The zipcodes nearby string is " + str(enduser.zipcodes_nearby) + "."
    else:
        enduser.zipcodes_nearby = str(zipcodes_nearby)
        enduser.save()
        responsemessage = "The zipcode_nearby string was empty on the User Table for " + str(enduser.email) + "."     
        new_zipnearby_string = enduser.zipcodes_nearby
        responsemessage = " The table has been updated. The zipcodes_nearby string is: " + str(new_zipnearby_string) + "."
    responsemessage = responsemessage + " The zipcodes in a " + str(mileradius) + " mile radius of " + str(enduser.email) + " are: " + str(zipcodes_nearby) + "."
    return responsemessage