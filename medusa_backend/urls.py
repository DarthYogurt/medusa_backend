from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

from soplog.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medusa_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^checklist/groupid/(\d*)/$', checklistSearchByGroupId),
    url(r'^checklist/checklistid/(\d*)/$', checklistSteps),
    url(r'^upload/$', upload), 
    url(r'^showLog/$', showLog),
    url(r'^analytics/$', analytics),
    url(r'^getLogData/(\d*)/$', getLogData),
    url(r'^slate/$', slate),
    url(r'^getSlate/$', getSlate),
#     url(r'^testPost/$', testPost),
    url(r'^testFile/$', testFile),  
    url(r'^latestPost/$', latestPost),
    
#     (r'^', include('soplog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),

    url(r'temp/$',temp),
#     url(r'^checklist/$', checkList),

#     
#     url(r'^createChecklist/$', createChecklist),
#     url(r'^listConfirm/$',listConfirm),
#     

#     url(r'^analytics/$', analytics),
#     
    

#     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT})
) 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
