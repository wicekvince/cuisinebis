from django.contrib import admin

from .models import Recette,  Ingredient,  Etape,  Photo

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre',)


class EtapeAdmin(admin.ModelAdmin):
    list_display = ('recette',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('recette',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recette',)


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Etape, EtapeAdmin)