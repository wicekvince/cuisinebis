from django.conf.urls import patterns, include, url
from .views import index
from django.contrib import admin
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', index, name='index'),

)
