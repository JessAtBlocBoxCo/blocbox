from django.conf.urls import patterns, include, url
from django.conf import settings
from testing import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		url(r'^$', 'testing.views.jesstest', name='testingbase'),    
 		url(r'^jesstest/$', 
 					'testing.views.jesstest', 
 					name='jesstestnohost')	
 					#kwargs={'host': [Year]}),
 						
 		url(r'^jesstest/$', 
 					'testing.views.jesstest', 
 					name='jesstestwithhost',	
 					kwargs={'host_id': 2}),
 			
 		url(r'^jesstest/(?P<userinfo_id>\d+)$', 'testing.views.jesstest', name='signupconnect'),
 		url(r'^styletest/$', 'testing.views.styletest', name='styletest'),
)

"""EXAMPLE OF HOW TO CALL SAME VIEW WITH DIFFERENT ARGS -- USE KWARGS

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
