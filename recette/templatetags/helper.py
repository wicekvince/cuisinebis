from django import template
from recette.models import Type, Recette


register = template.Library()


@register.inclusion_tag('recette/menu.html')
def show_menu():
    return {'types': Type.objects.all()}


@register.inclusion_tag('recette/nb_recette_total.html')
def show_nb_recette():
    return {'nb_total': Recette.objects.all().count()}