from django.conf.urls import patterns, include, url
from .views import index, register

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^accounts/register/$', register, name='register'),
)
