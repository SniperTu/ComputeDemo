from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views
 
import app.views
 
urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^compute/$', app.views.compute, name='compute'),
]