from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

		url(r'^$', views.index, name='index'),    
    url(r'beta/', views.beta, name='beta'), #Removing the caret so easier to hyperlink to
    url(r'^search/', views.search, name='search'),   
    url(r'^about/$', views.aboutblocbox, name='about'),
    url(r'^aboutblocbox/$', views.aboutblocbox, name='aboutblocbox'), 
    url(r'^hostprofile/host(?P<host_id>\d+)/$',views.hostprofile, name='hostprofile'),  
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dashboard/',views.dashboard, name='dashboard'),  
    url(r'^myblock/',views.myblock, name='myblock'),  
    url(r'^startashipment/$', views.startashipment, name='startashipment'),
    url(r'^nav_startashipment/$', views.nav_startashipment, name='nav_startashipment'),
    url(r'^nav_startafavor/$', views.nav_startafavor, name='nav_startafavor'),
    url(r'^startashipment/host(?P<host_id>\d+)/$', views.startashipment, name='startashipment'),
    url(r'^startashipment/host(?P<host_id>\d+)/days(?<dayrangestart>\d+)to(?<dayrangeend>\d+)/$', views.startashipment, name='startashipmentdays'),
    url(r'^startafavor/$', views.startafavor, name='startafavor'),
    url(r'^startafavor/host(?P<host_id>\d+)/$', views.startafavor, name='startafavor'),
    url(r'^shippackage/$', views.shippackage, name='shippackage_nohost'),  #this shouldn't really be used b/c not linked to a host  
    url(r'^shippackage/host(?P<host_id>\d+)/$', views.shippackage, name='shippackage'),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^signupconnect/host(?P<host_id>\d+)/$', views.signupconnect, name='signupconnect'),
    url(r'^connect/host(?P<host_id>\d+)/$', views.connectnewhost, name='connectnewhost'),
    url(r'^signup/', views.signupnoconnect, name='signupnoconnect'), 
    url(r'^hostsignup/', views.signuphost, name='signuphost'),
    url(r'^abouthosting/', views.abouthosting, name='abouthosting'),
    url(r'^nudgeaneighbor/', views.nudgeaneighbor, name='nudgeaneighbor'),
    url(r'^login/', views.userlogin, name='login'), # add this for the registration form
    url(r'^logout/$', views.user_logout, name='logout'), 		
    url(r'^almostfinished/$', views.waitlist_almostfinished, name='waitlist_almostfinished'),
    url(r'^waitlistconfirmation/$', views.waitlist_confirmation, name='waitlist_confirmation'),
 		#NOTE - removing the caret ^ before register so blocbox/register calls this as well
 		#the carret sasy beginning must match, the $ says end of string must match
 		#email stuff
 		url(r'^email/(?P<userinfo_id>\d+)/sendconfirmrequest/$', views.confirmconnect_mail, name='sendrequestconnect'),
    url(r'^(?P<host_id>\d+)/requestconnectconfirm/(?P<user_id>\d+)/$', views.confirmrequestconnect, name='confirmrequestconnect'), 		
 		url(r'^testing/', include('testing.urls')),
 		url(r'^scheduling/', include('schedule.urls')),
 		url(r'^passwordreset/',include('password_reset.urls')),
 		url(r'^messages/', include('django_messages.urls')),
 		url(r'^scheduling/', include('schedule.urls')),
 		#url(r'^payment/', views.payment, name='payment'),
 		url(r'^payment/', include('billing.urls', namespace='payment')), #because of the namepsac,e need to reeverse with reverse(payment:)
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
