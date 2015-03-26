from django.contrib import admin

from .models import Recette,  Ingredient,  Etape,  Photo


class EtapeAdmin(admin.StackedInline):
    model = Etape

class IngredientAdmin(admin.StackedInline):
    model = Ingredient


class PhotoAdmin(admin.StackedInline):
    model = Photo


class RecetteAdmin(admin.ModelAdmin):
    inlines = [ EtapeAdmin,IngredientAdmin,PhotoAdmin ]


admin.site.register(Recette, RecetteAdmin)