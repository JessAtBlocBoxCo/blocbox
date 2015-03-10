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
#json
import json
jsonDec = json.decoder.JSONDecoder()

#GET A LIST OF ALL TRANSACTIONS ON AFTERHIP
transactions_onaftership = Transaction.objects.filter(on_aftership=True)


def get_zipcodes_nearby(userid):
    enduser = UserInfo.objects.get(pk=userid)
    responsemessage = None
    mileradius = enduser.zipcodes_nearby_mileradius
    zip = enduser.zipcode
    zipcode = zcdb[zip]
    zipnearby_string = enduser.zipcodes_nearby
    zipnearby_list = jsonDec.decode(zipnearby_string)
    if zipnearby_string:
        responsemessage = "The zipcode_nearby string is on the User Table for " + str(enduser.email) \
            + ". The zipcodes within " + str(mileradius) + " miles are " + str(enduser.zipcodes_nearby) + "."
    else:
        responsemessage = "The zipcode_nearby string is empty on the User Table for " + str(enduser.email) + "." 
    if zipnearby_string:
        responsemessage = responsemessage + " Testing separating the string into elements separated by comma : "
        eachzip = ""
        for zip in zipnearby_list:
            eachzip = eachzip + str(zip) + ", "
        responsemessage = responsemessage + str(eachzip)
    return responsemessage

def add_zipcodes_nearby(userid, mileradius):
    enduser = UserInfo.objects.get(pk=userid)
    responsemessage = None
    zip = enduser.zipcode
    zipcode = zcdb[zip]
    zipnearby_string = enduser.zipcodes_nearby
    zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, mileradius)]
    zipcodes_nearby_json = json.dumps(zipcodes_nearby)
    enduser.zipcodes_nearby = zipcodes_nearby_json
    enduser.save()    
    new_zipnearby_string = enduser.zipcodes_nearby
    responsemessage = " The table has been updated. The zipcodes_nearby string is: " + str(new_zipnearby_string) + "."
    responsemessage = responsemessage + " The zipcodes in a " + str(mileradius) + " mile radius of " + str(enduser.email) + " are: " + str(zipcodes_nearby) + "."
    return responsemessage

def delete_zipcodes_nearby():
    users_all = UserInfo.objects.all()
    responsemessage = ""
    for user in users_all:
        user.zipcodes_nearby = None
        user.save()
        responsemessage = responsemessage + "The zipcode_nearby entry was deleted for " + str(user.email) + "."
    return responsemessage

def add_zipcodes_nearby_all():
    users_all = UserInfo.objects.all()
    responsemessage = ""
    for user in users_all:
        zip = user.zipcode
        if user.zipcodes_nearby_mileradius:
            mileradius = user.zipcodes_nearby_mileradius
        else:
            mileradius = 2
        zipcode = zcdb[zip]
        zipcodes_nearby = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, mileradius)]
        zipcodes_nearby_json = json.dumps(zipcodes_nearby)
        user.zipcodes_nearby = zipcodes_nearby_json
        user.save()
        responsemessage = responsemessage + "The zipcode_nearby entry was added for " + str(user.email) \
            + ". The zipcodes within a " + str(mileradius) + " mile radius are: " + str(zipcodes_nearby) + "."
    return responsemessage

def set_default_mileradius_task(mileradius):
    users_all = UserInfo.objects.all()
    for user in users_all:
        user.zipcodes_nearby_mileradius = mileradius
        user.save()
    responsemessage = "The mileradius for all users has been set to " + str(mileradius) + " miles."
    return responsemessage

def set_mileradius_user_task(userid, mileradius):
    enduser = UserInfo.objects.get(pk=userid)
    enduser.zipcodes_nearby_mileradius = mileradius
    enduser.save()
    responsemessage = "The mileradius variable has been set to " + str(mileradius) + " for user " + str(enduser.email) + "."
    return responsemessage

def add_neighbors_nearby_task():
    users_all = UserInfo.objects.all()
    for user in users_all:
        zip = user.zipcode
        zipcode = zcdb[zip]
        zipcodes_1mile = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 1)]
        zipcodes_2mile = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 2)]
        zipcodes_3mile = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 3)]
        zipcodes_4mile = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 4)]
        zipcodes_5mile = [z.zip for z in zcdb.get_zipcodes_around_radius(zipcode.zip, 5)]
        users_1mile = []
        users_2mile = []
        users_3mile = []
        users_4mile = []
        users_5mile = []
        for zip in zipcodes_1mile:
    	      users= UserInfo.objects.filter(zipcode=zip)
    	      users_1mile.append(users)
        for zip in zipcodes_2mile:
    	      users = UserInfo.objects.filter(zipcode=zip)
    	      users_2mile.append(users)
        for zip in zipcodes_3mile:
            users = UserInfo.objects.filter(zipcode=zip)
            users_3mile.append(users)
        for zip in zipcodes_4mile:
            users = UserInfo.objects.filter(zipcode=zip)
            users_4mile.append(users)
        for zip in zipcodes_5mile:
            users = UserInfo.objects.filter(zipcode=zip)
            users_5mile.append(users)
        user.neighbors_1mileradius = json.dumps(users_1mile)
        user.neighbors_2mileradius = json.dumps(users_2mile)
        user.neighbors_3mileradius = json.dumps(users_3mile)
        user.neighbors_4mileradius = json.dumps(users_4mile)
        user.neighbors_5mileradius = json.dumps(users_5mile)
    return "Users were added for 1, 2, 3, 4, 5 mile radius"