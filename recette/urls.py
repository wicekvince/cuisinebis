from django.conf.urls import patterns, include, url
from .views import index
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import index, recette

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^recette/(?P<id>\d+)/', recette, name="recette"),

)
