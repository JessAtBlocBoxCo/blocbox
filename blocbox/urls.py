from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

		url(r'^$', views.index, name='index'),    
    url(r'beta/', views.beta, name='beta'), #Removing the caret so easier to hyperlink to
    url(r'^search/', views.search, name='search'),    
    url(r'^(?P<userinfo_id>\d+)/hostprofilevisitor/$',views.hostprofilevisitor, name='hostprofilevisitor'),  
    #url(r'^hostprofile/', include('hostprofile.urls', namespace="hostprofile")),
    #url(r'^messages/', include('messages.urls', namespace="messages")),
    #url(r'^payment/', include('payment.urls', namespace="payment")),
    #url(r'^polls/', include('polls.urls', namespace="polls")), #INCLUDE the URLconf at blocbox/polls
    url(r'^admin/', include(admin.site.urls)), #INCLUDE the URLconf at 
    url(r'^(?P<userinfo_id>\d+)/signupconnect/$', views.signupconnect, name='signupconnect'),
    url(r'signup/', views.signupnoconnect, name='signupnoconnect'), 
    url(r'signuphost/', views.signuphost, name='signuphost'),
    url(r'login/', views.userlogin, name='login'), # add this for the registration form
    url(r'^logout/$', views.user_logout, name='logout'), 		
 		#NOTE - removing the caret ^ before register so blocbox/register calls this as well
 		#the carret sasy beginning must match, the $ says end of string must match
 		#try geeric welcomebeta view - then apply generics to other sites
 		#Can delete the following - for testing the login view
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
