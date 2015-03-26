from django.conf.urls import patterns, include, url
from .views import index, register
from .views import index, recette, nouvelleRecette


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^recette/(?P<id>\d+)/', recette, name="recette"),
    url(r'^ajouter$', nouvelleRecette, name="ajout"),
    url(r'^account/register/$', register, name='register'),
)




