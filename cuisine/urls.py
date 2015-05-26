from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name="logout"),
    url(r'^', include('recette.urls', namespace='recette')),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))