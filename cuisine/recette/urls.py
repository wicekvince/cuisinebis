from django.conf.urls import patterns, include, url
from .views import index, detail, resultats, voter, IndexView, test


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'formation.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^question/(?P<id>\d+)/$', detail, name='detail'),
                       url(r'^question/(?P<id>\d+)/resultats/$', resultats, name='resultats'),
                       url(r'^voter/(?P<id>\d+)/$', voter, name='voter'),
                       url(r'^test/$', test, name='test'),
                       )
