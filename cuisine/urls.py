from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', 'django.contrib.auth.views.login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^', include('recette.urls', namespace='recette')),
)
