from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

		url(r'^$', views.index, name='index'),    
    url(r'beta/', views.beta, name='beta'), #Removing the caret so easier to hyperlink to
    url(r'^search/', views.search, name='search'),   
    url(r'^searchold/', views.searchold, name='searchtest'),  
    url(r'^(?P<userinfo_id>\d+)/hostprofile/$',views.hostprofile, name='hostprofile'),  
    url(r'^dashboard/',views.dashboard, name='dashboard'),  
    url(r'^startashipment/', views.startashipment, name='startashipment'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^shippackage/', views.shippackage, name='shippackage'),     
    #url(r'^payment/', include('payment.urls', namespace="payment")),
    #url(r'^polls/', include('polls.urls', namespace="polls")), #INCLUDE the URLconf at blocbox/polls
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^(?P<userinfo_id>\d+)/signupconnect/$', views.signupconnect, name='signupconnect'),
    url(r'signup/', views.signupnoconnect, name='signupnoconnect'), 
    url(r'signuphost/', views.signuphost, name='signuphost'),
    url(r'login/', views.userlogin, name='login'), # add this for the registration form
    url(r'^logout/$', views.user_logout, name='logout'), 		
    url(r'^bootstraptest/$', views.bootstraptest, name='bootstraptest'),
    url(r'^almostfinished/$', views.waitlist_almostfinished, name='waitlist_almostfinished'),
    url(r'^waitlistconfirmation/$', views.waitlist_confirmation, name='waitlist_confirmation'),
 		#NOTE - removing the caret ^ before register so blocbox/register calls this as well
 		#the carret sasy beginning must match, the $ says end of string must match
 		#email stuff
 		url(r'^email/(?P<userinfo_id>\d+)/sendconfirmrequest/$', views.confirmconnect_mail, name='sendrequestconnect'),
    url(r'^(?P<host_id>\d+)/requestconnectconfirm/(?P<user_id>\d+)/$', views.confirmrequestconnect, name='confirmrequestconnect'), 		
    url(r'^styletest/$', views.styletest, name='styletest'),
 		url(r'^jesstest/$', views.jesstest, name='jesstest'),
 		
 		url(r'^passwordreset/',include('password_reset.urls')),
 		url(r'^messages/', include('django_messages.urls')),
 		url(r'^payment/paypal/', include('paypal.standard.ipn.urls')),
 		url(r'^datascience/', include('datasci.urls')),
 		
)



urlpatterns += staticfiles_urlpatterns()

#if want to import generic index view will look like
#url(r'^$', views.IndexView.as_view(), name='index'),
#url(r'^old/', views.oldindex, name='oldindex'), #old index

"""INCLUDE: when django ecounters include() it chops off whatever part matched and sents rest of the string
to the included URLconf for futher processing - so polls URLS are in their own URLconf polls.urls.py - they can be put aywhere
"""
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
