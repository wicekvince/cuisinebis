from django.conf.urls import patterns, include, url
from .views import index, register
from .views import index, recette

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^recette/(?P<id>\d+)/', recette, name="recette"),
    url(r'^accounts/register/$', register, name='register'),
)




