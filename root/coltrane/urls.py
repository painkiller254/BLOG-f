from django.conf.urls import *
from django.urls import path
from coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

url_patterns = [
    path(r'', include('django.contrib.flatpages.urls')),
    path(r'^$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    path(r'^(?P<year>\d{4}/$', 'django.views.generic.date_based.archive_year', entry_info_dict),
    path(r'^(?P<year>\d{4}/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict),
    path(r'^(?P<year>\d{4}/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict),
    path(r'^(?P<year>\d{4}/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail', entry_info_dict),
]