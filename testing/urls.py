from django.conf.urls import patterns, include, url
from django.conf import settings
from testing import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

#all url patterns preceded by blocbox.co/testing
urlpatterns = patterns('',
		url(r'^$', 'testing.views.jesscaltest', name='testingbase'),   #default view is calendar test 		
 		url(r'^dashboard/$', 'testing.views.dashboard_test', name='dashboard_test'),
 		url(r'^jesstest/$', 'testing.views.jesscaltest', name='jesstestnohost'), 	
 		url(r'^homebrewcal/', 'testing.views.homebrew_cal', name='homebrew_cal'),	
 		url(r'^facebook/', 'testing.views.facebook', name='test_facebook'),
 		url(r'^sendfacebookdata/', 'testing.views.sendfacebookdata', name='test_sendfacebookdata'),	
 		url(r'^ajax_test/', 'testing.views.ajax_test', name='ajax_test'),			
 		#pass the same test but with a host_id in the URL - dont need a KWARG explicit statmenet bc it is passed in the URL name
 		url(r'^jesstest/host(?P<host_id>\d+)/$', 'testing.views.jesscaltest', name='jesstestwithhost'),	 		
 		url(r'^styletest/$', 'testing.views.styletest', name='styletest'),
 		url(r'^aftership/$', 'testing.views.aftership', name='aftership_test'),
 		url(r'^bootstraptest/$', 'testing.views.bootstraptest', name='bootstraptest'),
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
