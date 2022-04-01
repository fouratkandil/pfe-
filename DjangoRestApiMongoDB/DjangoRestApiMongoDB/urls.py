from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('environment.urls')),
]
