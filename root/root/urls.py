from django.contrib import admin
from django.urls import path, include
from django.conf.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('django.contrib.flatpages.urls')),
    path(r'^weblog/', include('coltrane.urls')),
    
    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags/', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
]
