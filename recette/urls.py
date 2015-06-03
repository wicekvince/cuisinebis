from django.conf.urls import patterns, include, url
from .views import index, recette, register, nouvelleRecette, search, mes_recettes, supprimerRecette, modifyRecette


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^recette/(?P<id>\d+)/', recette, name="recette"),
    url(r'^ajouter$', nouvelleRecette, name="ajout"),
    url(r'^account/register/$', register, name='register'),
    url(r'^search_result/$', search, name='search'),
    url(r'^mes_recettes/$', mes_recettes, name='mesrecettes'),
    url(r'^supprimer_recette/(?P<id>\d+)/', supprimerRecette, name='supprimerrecette'),
    url(r'^modify_recette/(?P<id>\d+)/', modifyRecette, name='modify_recette'),
)




