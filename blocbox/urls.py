from django.conf.urls import patterns, include, url
from core import views #it imports views from blocbox modeule so knows where to look for index files, cneed to ref new URL page sso 'view' means another app in another context
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

		url(r'^$', views.waitlist, name='waitlist'),    #this currently grabs index.html which is the waitlist
	  url(r'^referredby=(?P<referring_user_email>[^/]+)/$', views.waitlist, name='waitlist_ref'),
		url(r'^bloc=(?P<neighborhood>\w+)/$', views.waitlist, name='waitlist_bloc'),
		url(r'^bloc=(?P<neighborhood>\w+)/referredby=(?P<referring_user_email>[^/]+)/$', views.waitlist, name='waitlist_ref_bloc'),
        url(r'^clintonhill/$', views.waitlist, {'neighborhood': 'clintonhill'},  name='waitlist_ch'),
        url(r'^clintonhill/referredby=(?P<referring_user_email>[^/]+)/$', views.waitlist, {'neighborhood': 'clintonhill'}, name='waitlist_ref_bloc'),
        url(r'^brooklyn/$', views.waitlist, {'neighborhood': 'brooklyn'}, name='waitlist_bk'),
        url(r'^brooklyn/referredby=(?P<referring_user_email>[^/]+)/$', views.waitlist, {'neighborhood': 'brooklyn'}, name='waitlist_ref_bloc'),
		url(r'^waitlist/', views.waitlist, name='waitlist'), #also goes to the waitlist
    
    url(r'^joinwaitlist/$', views.joinwaitlist, name='joinwaitlist'),
    url(r'^joinwaitlist_noajax/$', views.joinwaitlist_noajax, name='joinwaitlist_noajax'),
    url(r'^joinwaitlist/referredby=(?P<referring_user_email>[^/]+)/$', views.joinwaitlist, name='joinwaitlist_referral'), 
    
    url(r'^joinwaitlist/clintonhill/$', views.joinwaitlist, {'neighborhood': 'clintonhill'}, name='joinwaitlist_ch'),
    url(r'^joinwaitlist/brooklyn/$', views.joinwaitlist, {'neighborhood': 'brooklyn'}, name='joinwaitlist_bk'),
    url(r'^joinwaitlist/clintonhill/referredby=(?P<referring_user_email>[^/]+)/$',  views.joinwaitlist, {'neighborhood': 'clintonhill'}, name='joinwaitlist_ref_ch'),
    url(r'^joinwaitlist/brooklyn/referredby=(?P<referring_user_email>[^/]+)/$',  views.joinwaitlist, {'neighborhood': 'brooklyn'}, name='joinwaitlist_ref_bk'),


    url(r'beta/$', views.beta, name='beta'), #Removing the caret so easier to hyperlink to
    url(r'^search/', views.search, name='search'),   
    #url(r'^searchtest/', views.search_test, name='delmesearch'),
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
                       
    url(r'^hostdashboard/$',views.dashboard_host, name='host_dashboard'),
    url(r'^hostdashboard/confirm_id(?P<confirm_id>\d+)/',views.dashboard_host, name='host_dashboard'),
                       
    


    #Simple sign up (in use)
    url(r'^signup/$', views.signup, name='signupsimple_noconnect'), 
    url(r'^signup/host(?P<host_id>\d+)/$', views.signup, name='signupsimple', ),
    url(r'^signup/host(?P<host_id>\d+)/referredby=(?P<referring_user_email>[^/]+)/$', views.signup, name='signupsimple_ref', ),
    url(r'^signup/bloc=(?P<neighborhood>\w+)/$', views.signup, name='signupsimplebloc', ),
    url(r'^signup/bloc=(?P<neighborhood>\w+)/$', views.signup, name='signupsimplebloc_ref', ),
    #Simple sign up for host
    url(r'^signuphost/$', views.signup, {'hostsignup': True }, name='signupsimple_host'), 

    
    #OBE - long - sign up no connect
    url(r'^signuplong/$', views.signup, {'templatename': 'signuplong/sign-up-withoutconnect' }, name='signupnoconnect'), 
    url(r'^signuplong/referredby=(?P<referring_user_email>[^/]+)/$', views.signup, {'templatename': 'sign-up-withoutconnect' }, name='signupnoconnect_referral'), 
    #OBE - long - sign up connect - via host or via bloc		
    url(r'^signuplong/host(?P<host_id>\d+)/$', views.signup, {'templatename': 'signuplong/sign-up-connect' }, name='signupconnect'),
    url(r'^signuplong/host(?P<host_id>\d+)/referredby=(?P<referring_user_email>[^/]+)/$', views.signup, {'templatename': 'signuplong/sign-up-connect' }, name='signupconnect_ref',),            
    url(r'^signuplong/bloc=(?P<neighborhood>\w+)/$', views.signup, {'templatename': 'signuplong/sign-up-connect' }, name='signupconnectbloc', ),
    url(r'^signuplong/bloc=(?P<neighborhood>\w+)/$', views.signup, {'templatename': 'signuplong/sign-up-connect' }, name='signupconnectbloc_ref', ),
    #OBE - Host sign up - based on simple sign up	
    url(r'^signuplonghost/$', views.signuplong_host, name='signuphost'),
    
    url(r'^connect/host(?P<host_id>\d+)/$', views.connectnewhost, name='connectnewhost'),
    url(r'^abouthosting/', views.abouthosting, name='abouthosting'),
    url(r'^nudgeaneighbor/', views.nudgeaneighbor, name='nudgeaneighbor'),
    url(r'^login/', views.userlogin, name='login'), # add this for the registration form
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^almostfinished/$', views.waitlist_almostfinished, name='waitlist_almostfinished'),
   
    url(r'^testsendtomailchimp/user(?P<waitlistuserid>\d+)/$', views.send_form_to_mailchimp, name='test_sentomailchimp'),
    url(r'^waitlistconfirmation/$', views.waitlist_confirmation, name='waitlist_confirmation'),
 		#NOTE - removing the caret ^ before register so blocbox/register calls this as well
 		#the carret sasy beginning must match, the $ says end of string must match
 		#email stuff
 		url(r'^email/(?P<userinfo_id>\d+)/sendconfirmrequest/$', views.confirmconnect_mail, name='sendrequestconnect'),
    url(r'^(?P<host_id>\d+)/requestconnectconfirm/(?P<user_id>\d+)/$', views.confirmrequestconnect, name='confirmrequestconnect'), 		
 	url(r'^testing/', include('testing.urls')),
 	
    #url(r'^scheduling/', include('schedule.urls')),
 	url(r'^passwordreset/',include('password_reset.urls')),
 	url(r'^messages/', include('django_messages.urls')),
 	#url(r'^datascience/', include('datasci.urls')),
    url(r'^editprofile/$', views.editprofile, name='editprofile'),
        url(r'^editprofilefrom(?P<from_page>\w+)/$', views.editprofile, name='editprofile_from_page', ),
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
