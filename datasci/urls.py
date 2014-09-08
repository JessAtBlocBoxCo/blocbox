from django.conf.urls import patterns, include, url
from django.contrib import admin
from core import views 

admin.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datasci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'datascience/', views.datascience_home, name='datasci'), #Removing the caret so easier to hyperlink to
    
)
