from django.conf.urls import patterns, include, url
from django.contrib import admin
from datasci import views 

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datasci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
		url(r'^$', views.index, name='index'), 
    #url(r'datascience/', views.datascience_home, name='datasci'), #Removing the caret so easier to hyperlink to
  
    
)
