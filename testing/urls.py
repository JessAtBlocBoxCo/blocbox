from django.conf.urls import patterns, include, url
from testing import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
		url(r'^$', testing.views.jesstest, name='testingbase'),    
 		url(r'^jesstest/$', testing.views.jesstest, name='jesstest'),		
 		url(r'^styletest/$', testing.views.styletest, name='styletest'),
)

urlpatterns += staticfiles_urlpatterns()


from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
