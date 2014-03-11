from django.conf.urls import patterns
from fileupload.views import *

urlpatterns = patterns('',
                       (r'^new/$', MediaFileCreateView.as_view(), {}, 'upload-new'),
                       (r'^delete/(?P<pk>\d+)$', MediaFileDeleteView.as_view(), {}, 'upload-delete'),
)

