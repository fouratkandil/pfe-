from django.urls import re_path as url
from environment import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^DjangoRestApiMongoDB/environment$', views.environmentApi),
]
