from django.contrib import admin
from django.urls import path, include
from django.conf.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('django.contrib.flatpages.urls')),
    path(r'^weblog/', include('coltrane.urls'))
]
