from django import template
from recette.models import Type
register = template.Library()

@register.inclusion_tag('recette/menu.html')
def show_menu():
      return {'types': Type.objects.all()}