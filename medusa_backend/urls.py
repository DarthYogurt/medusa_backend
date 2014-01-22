from django.conf.urls import patterns, include, url
from django.contrib import admin


from soplog.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medusa_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage)
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^checklist/$', checkList),
#     url(r'^checklist/groupid/(\d*)/$', checklistSearchByGroup),   
#     url(r'^checklist/checklistid/(\d*)/$', checklistSteps),
#     url(r'^createChecklist/$', createChecklist),
#     url(r'^listConfirm/$',listConfirm),
#     url(r'^upload/$', upload), 
#     url(r'^showLog/$', showLog),
#     url(r'^analytics/$', analytics),
#     url(r'^getLogData/(\d*)/$', getLogData),
    
    
)
