#This is blocbox/transactions/urls.py
from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files
#from django.conf.urls.defaults import * #that was in the paypal ipn
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from transactions import views 
from paypal.standard.ipn import views
admin.autodiscover()


#url patterns preceded by blocbox.co/transactions (e.g., www.blocbox.co/transactions/startashipment) - the namespace is transactions, so need to reverse call with, eg payment:paypal_ipn
urlpatterns = patterns('',
		#Base views - defined in transactions/views.py
		url(r'^$', 'paypal.standard.ipn.views.ask_for_money', name='payment_default'), #blocbox.co/transactions, defaults o host_id=2 which is John
		url(r'^startashipment/$', 'transactions.views.startashipment', name='startashipment'),
    url(r'^nav_startashipment/$', 'transactions.views.nav_startashipment', name='nav_startashipment'),
    url(r'^nav_startafavor/$', 'transactions.views.nav_startafavor', name='nav_startafavor'),
    url(r'^startashipment/host(?P<host_id>\d+)/$', 'transactions.views.startashipment', name='startashipment'),
    url(r'^startashipment/host(?P<host_id>\d+)/trans_submitted(?P<transaction_form_submitted>\w+)/invoice(?P<invoice>\w+)/$', 'transactions.views.startashipment', name='startashipmentdays'),
    url(r'^startashipment/host(?P<host_id>\d+)/cal_form_submitted(?P<cal_form_submitted>\w+)/invoice(?P<invoice>\w+)/packagedays_count(?P<packagedays_count>\d+)/$', 'transactions.views.startashipment', name='startashipmentdays'),
    url(r'^startafavor/$', 'transactions.views.startafavor', name='startafavor'),
    url(r'^startafavor/host(?P<host_id>\d+)/$', 'transactions.views.startafavor', name='startafavor'),
    url(r'^shippackage/$', 'transactions.views.shippackage', name='shippackage_nohost'),  #this shouldn't really be used b/c not linked to a host  
    url(r'^shippackage/host(?P<host_id>\d+)/$', 'transactions.views.shippackage', name='shippackage'),
		url(r'^shippackage/host(?P<host_id>\d+)/account_balance/trans_id(?P<trans_id>\d+)/$', 'transactions.views.shippackage_accountbalance', name='shippackage_accountbalance'),
		#SHIPMENTthe blocbox.paypal.standard.ipn.views.ask_for_money view triggered by a SHIPMENT - with dayrangestart, danrange end
    url(r'^payment/host(?P<host_id>\d+)/invoice(?P<invoice>\w+)/favortype(?P<favortype>\w+)/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask_shipment'),
		#FAVORthe blocbox.paypal.standard.ipn.views.ask_for_money view triggered by a FAVOR (e.g., no dayrangestart or dayrange end)
		url(r'^payment/host(?P<host_id>\d+)/ipn/(?P<favortype>\w+)/(?P<paymentoption>\w+)/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask_favor'),
		#Notify URL for paypal IPAN
		url(r'^ipn/notify(?P<host_id>\d+)/(?P<trans_id>\d+)/$', 'paypal.standard.ipn.views.ipn', name='paypal_ipn_notify'), 
		url(r'^ipn/$', 'paypal.standard.ipn.views.ask_for_money', name='ipn_ask_nohost'), #blocbox.co/payment/ipn - NOT FUNCTION B/C DOESN'T LINK TO HOST
    url(r'^ipn/return/$', 'paypal.standard.ipn.views.ipn_return_successful', name='ipn_return_successful'), #Eventually may need a return URL
    url(r'^testnotifyenduser/$', 'paypal.standard.ipn.views.test_notify_enduser_shipment_paid', name='test_notify'),
    #STANDARD-PDT URLS
    #PRO URLS
    #url(r'^pro$', 'transactions.views.paypal_pro', name='paypalpro'), #no real purpose to this bc not linked to a host
    #url(r'^host(?P<host_id>\d+)/pro/(?<paymentoption>\w+)/$', 'transactions.views.paypal_pro', name='paypalpro'),        
 		#url(r'^checkout/$', 'transactions.views.checkout', name='checkoutgeneric'),
 		#url(r'^checkout/host(?P<host_id>\d+)/$', 'transactions.views.checkout', name='checkoutuser'),
 		#url(r'^paypal', 'transactions.views.paypal_askformoney', name='paypalbase'), 	
)

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
