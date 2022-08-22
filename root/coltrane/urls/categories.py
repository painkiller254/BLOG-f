from django.conf.urls import *
from django.urls import patterns
from coltrane.models import Category

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Category.objects.all() }),
    (r'^(?P<slug>[-\w]+)/$', 'coltrane.views.category_detail'),
)