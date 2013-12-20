from django.conf.urls import patterns, include, url
from django.contrib import admin

from medusa_backend.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medusa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$',hello),
    #url(r'^hello/', 'medusa.views.hello', name='hello'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', currentTime),
    
    url(r'^time/plus/(\d{1,2})/$', hoursAhead),
    url(r'^name/([^/]+)/$', myName),
    url(r'^template/([^/]+)/$', template),
    url(r'^$', homepage),
)
