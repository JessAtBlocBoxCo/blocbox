#This is blocbox/billing/urls.py
from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files
#from django.conf.urls.defaults import * #that was in the paypal ipn
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from billing import views 
from paypal.standard.ipn import views
admin.autodiscover()


#url patterns preceded by blocbox.co/payment - the namespace is payment, so need to reverse call with, eg payment:paypal_ipn
urlpatterns = patterns('',
		#Base views - defined in billing/views.py
		url(r'^$', 'paypal.standard.ipn.views.ask_for_money', name='payment_default'), #blocbox.co/payment
		url(r'^host(?P<host_id>\d+)/$', 'billing.views.base', name='billingbase'), #blocbox.co/payment/host2
		#STANDARD-IPN URLs - view in paypal/standard/ipn/views.py
		url(r'^host(?P<host_id>\d+)/ipn/(?P<paymentoption>\w+)/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask'), #blocbox.co/payment/host2/<TYPE?
		url(r'^ipn/host(?P<host_id>\d+)/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask_noamount'), #blocbox.co/payment/host2 - not really relevant - Default - Package Amount
		url(r'^ipn/notify', 'paypal.standard.ipn.views.ipn', name='paypal_ipn_notify'), #this is the notify_url	
		url(r'^ipn/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask_nohost'), #blocbox.co/payment/ipn - NOT FUNCTION B/C DOESN'T LINK TO HOST
    url(r'^ipn/return/$', 'paypal.standard.ipn.views.ipn_return_successful', name='ipn_return_successful'), #Eventually may need a return URL
    #STANDARD-PDT URLS
    #PRO URLS
    #url(r'^pro$', 'billing.views.paypal_pro', name='billingpro'), #no real purpose to this bc not linked to a host
    #url(r'^host(?P<host_id>\d+)/pro/(?<paymentoption>\w+)/$', 'billing.views.paypal_pro', name='billingpro'),        
 		#url(r'^checkout/$', 'billing.views.checkout', name='checkoutgeneric'),
 		#url(r'^checkout/host(?P<host_id>\d+)/$', 'billing.views.checkout', name='checkoutuser'),
 		#url(r'^paypal', 'billing.views.paypal_askformoney', name='paypalbase'), 	
)

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
