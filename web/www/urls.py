from django.conf.urls.defaults import *

urlpatterns = patterns('www.views',
    url(r'^$', 'index', name='www_index'),
)
