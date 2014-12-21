#this is blocbox.core.modaltags.py, its imported by core.views.py creates views to render modals

import datetime
from django.conf import settings
from schedule.conf.settings import CHECK_EVENT_PERM_FUNC, CHECK_CALENDAR_PERM_FUNC
from django import template
from django.template import RequestContext, loader #allows it to load templates from blocbox/templates
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
#Add CORE and TRANSACTIONS models
from core.models import UserInfo
from connections.models import Connection
from transactions.models import Transaction
#from django.contrib.auth.models import User #dont need this because not using User - maybe why it create table..
from core.forms import UserForm, HostForm
from connections.forms import ConnectForm
from transactions.forms import TrackingForm, ModifyTransaction
#Important the authentication and login functions -- not sure that i can use with custom model
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
#import some generic stuff
import datetime
import pytz
from django.utils.dateformat import format
from urllib import quote
from django.utils import timezone
#import schedule and billing stuff
from schedule.periods import Month
from schedule.periods import weekday_names
from schedule.conf.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT
from schedule.forms import EventForm, OccurrenceForm
from schedule.models import Calendar, Occurrence, Event
from paypal.standard.ipn.models import PayPalIPN

register = template.Library()

#Write a custom template filter:
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

#create a view to call the trackin gmodal
#call it with {% tracking_modal trans_id %} so with shipments ill be {% tracking_modal shipment.id %}
@register.inclusion_tag("modals/trackingmodal.html")
def tracking_modal(request, trans_id):
    #Add tracking info - a good example of modifying an existing model instead of creating a new one
    trans = Transaction.objects.get(pk=trans_id)
    invoice = trans.invoice
    if request.method == 'POST':        
        tracking_form  = TrackingForm(request.POST, instance=trans)
        if tracking_form.is_valid(): 
            trackadd = tracking_form.save()          
            trackadd.save()   	     
        else: 
    	      print tracking_form.errors 
    else:
        tracking_form = TrackingForm(instance=trans)   
    request_method = request.method    
    context = {
        'trans_id': trans_id, 
    	  'tracking_form': tracking_form, 'trans': trans, 'invoice': invoice,
    	  #tests
    	  'request': request, 'request_method': request_method,
    }
    return context	




"""
this was called with: {% prevnext "day_calendar" calendar.slug periods.day "l, F d, Y" %}

@register.inclusion_tag("schedule/_prevnext.html")
def prevnext(target, slug, period, fmt=None):
    if fmt is None:
        fmt = settings.DATE_FORMAT
    context = {
        'slug': slug,
        'period': period,
        'period_name': format(period.start, fmt),
        'target': target,
    }
    return context

# _prevnext.html looked like this: 

{% load scheduletags staticfiles %}

    <a href="{% prev_url target slug period %}">
      <img align="top" border="0" src="{% static "schedule/img/left_mod.png" %}"/>
    </a> 
    
    {{period_name}}  
    
    <a href="{% next_url target slug period %}">
      <img align="top" border="0" src="{% static "schedule/img/right_mod.png" %}"/>
    </a>


"""