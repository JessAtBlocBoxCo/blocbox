from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files, cneed to ref new URL page sso 'view' means another app in another context
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

		url(r'^$', views.waitlist, name='waitlist'),    #this currently grabs index.html which is the waitlist
		url(r'^waitlist/', views.waitlist, name='waitlist'), #also goes to the waitlist
    url(r'beta/$', views.beta, name='beta'), #Removing the caret so easier to hyperlink to
    url(r'^search/', views.search, name='search'),   
    url(r'^about/$', views.aboutblocbox, name='about'),
    url(r'^aboutblocbox/$', views.aboutblocbox, name='aboutblocbox'), 
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^support/$', views.contactus, name='contactus'),
    url(r'^hostprofile/host(?P<host_id>\d+)/$',views.hostprofile, name='hostprofile'),  
    url(r'^profile/$', views.profile, name='profile'),
                       
    url(r'^account/$', views.account, name='account'),
    url(r'^notifications/$', views.account, name='notifications'),
    url(r'^payment-options/$', views.paymentoptions, name='paymentoptions'),
    url(r'^past-transactions/$', views.pasttransactions, name='pasttransactions'),
    url(r'^security/$', views.security, name='security'),
    url(r'^settings/$', views.settings, name='settings'),     
                       
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    #need different URLs for the different modals on the dashboard - otherwise forms dont know what to submit
    url(r'^dashboard/track_id(?P<track_id>\d+)/',views.dashboard, name='dashboard'), 
    url(r'^dashboard/confirm_id(?P<confirm_id>\d+)/',views.dashboard, name='dashboard'),
    url(r'^dashboard/issue_id(?P<issue_id>\d+)/', views.dashboard, name='dashboard'),
    url(r'^dashboard/message_id(?P<message_trans_id>\d+)/', views.dashboard, name='dashboard'),
    url(r'^dashboard/archive_id(?P<archive_id>\d+)/', views.dashboard, name='dashboard'),
    url(r'^myblock/',views.myblock, name='myblock'),  
    #the transactions subdomain includes all of the start a shipment / start a favor and payment views
 		url(r'^transactions/', include('transactions.urls', namespace='transactions')), #because of the namepsac,e need to reeverse with reverse(payment:)
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^signupconnect/host(?P<host_id>\d+)/$', views.signupconnect, name='signupconnect'),
    url(r'^signupconnect/host(?P<host_id>\d+)/referredby=(?P<referring_user_email>[^/]+)/$', views.signupconnect, name='signupconnect_referral'),    
    url(r'^connect/host(?P<host_id>\d+)/$', views.connectnewhost, name='connectnewhost'),
    url(r'^signup/$', views.signupnoconnect, name='signupnoconnect'), 
    url(r'^signup/referredby=(?P<referring_user_email>[^/]+)/$', views.signupnoconnect, name='signupnoconnect_referral'),    
    url(r'^signuphost/$', views.signuphost, name='signuphost'),
    url(r'^abouthosting/', views.abouthosting, name='abouthosting'),
    url(r'^nudgeaneighbor/', views.nudgeaneighbor, name='nudgeaneighbor'),
    url(r'^login/', views.userlogin, name='login'), # add this for the registration form
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^almostfinished/$', views.waitlist_almostfinished, name='waitlist_almostfinished'),
    url(r'^joinwaitlist/$', views.joinwaitlist, name='joinwaitlist'),
    
    url(r'^joinwaitlist/referredby=(?P<referring_user_email>[^/]+)/$', views.joinwaitlist, name='joinwaitlist_referral'),    
    url(r'^testsendtomailchimp/user(?P<waitlistuserid>\d+)/$', views.send_form_to_mailchimp, name='test_sentomailchimp'),
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
 		#url(r'^datascience/', include('datasci.urls')),
    url(r'^editprofile/$', views.editprofile, name='editprofile'),
    url(r'^addinterest/$', views.addinterest, name='addinterest'),
 		
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
