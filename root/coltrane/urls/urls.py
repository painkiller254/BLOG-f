# from django.conf.urls import *
# from django.urls import path
# from coltrane.models import Entry, Link

# entry_info_dict = {
#     'queryset': Entry.objects.all(),
#     'date_field': 'pub_date',
# }

# link_info_dict = {
#     'queryset': Link.objects.all(),
#     'date_field': 'pub_date',
# }

# url_patterns = [
#     path(r'^$', 'django.views.generic.date_based.archive_index', entry_info_dict),
#     path(r'^(?P<year>\d{4}/$', 'django.views.generic.date_based.archive_year', entry_info_dict),
#     path(r'^(?P<year>\d{4}/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict),
#     path(r'^(?P<year>\d{4}/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict),
#     path(r'^(?P<year>\d{4}/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail', entry_info_dict),

#     path(r'^links/$', 'archive_index', link_info_dict, 'coltrane_link_archive_index'),
#     path(r'^links/(?P<year>\d{4})/$', 'archive_year', link_info_dict,'coltrane_link_archive_year'),
#     path(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/$',
# 'archive_month', link_info_dict,
# 'coltrane_link_archive_month'),
#     path(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', link_info_dict, 'coltrane_link_archive_day'),
#     path(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', link_info_dict, 'coltrane_link_detail'),
# ]