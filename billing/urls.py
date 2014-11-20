#This is blocbox/billing/urls.py
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import * #that was in the paypal ipn
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from billing import views 
from paypal.standard.ipn import views
admin.autodiscover()


#url patterns preceded by blocbox.co/payment
urlpatterns = patterns('',
		url(r'^$', 'billing.views.base', name='billingbase'),
		url(r'^ipn$', 'billing.views.paypal_ipn', name='billingipn'), 
    url(r'^pro$', 'billing.views.paypal_pro', name='billingpro'),      
 		url(r'^checkout/$', 'billing.views.checkout', name='checkoutgeneric'),
 		url(r'^checkout/host(?P<host_id>\d+)/$', 'billing.views.checkout', name='checkoutuser'),
 		url(r'^paypal', 'billing.views.paypal_askformoney', name='paypalbase'), 	
 		url(r'^ipn/notify', 'paypal.standard.ipn.views.ipn', name="paypalipn"), #this is the notify_url	
)



"""EXAMPLE OF HOW TO CALL SAME VIEW WITH DIFFERENT ARGS -- USE KWARGS

		url(r'^$', 'testing.views.jesstest', name='testingbase'),    
 		
 		url(r'^jesstest/$', 'testing.views.jesstest', name='jesstestnohost'),
 						
 		#pass the same test but with a host_id in the URL - dont need a KWARG explicit statmenet bc it is passed in the URL name
 		url(r'^jesstest/(?P<host_id>\d+)/$', 'testing.views.jesstest', name='jesstestwithhost'),	 		
 		url(r'^styletest/$', 'testing.views.styletest', name='styletest'),
 		
    url(r'^calendar/year/(?P<calendar_slug>[-\w]+)/$',
        'schedule.views.calendar_by_periods',
        name="year_calendar",
        kwargs={'periods': [Year], 'template_name': 'schedule/calendar_year.html'}),

    url(r'^calendar/tri_month/(?P<calendar_slug>[-\w]+)/$',
        'schedule.views.calendar_by_periods',
        name="tri_month_calendar",
        kwargs={'periods': [Month], 'template_name': 'schedule/calendar_tri_month.html'}),


"""
urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
