from django.contrib import admin
from .models import Recette,  Ingredient,  Etape,  Photo, Type
from django.contrib.auth.models import User


class EtapeAdmin(admin.StackedInline):
    model = Etape


class IngredientAdmin(admin.StackedInline):
    model = Ingredient


class IngredientAdmin2(admin.ModelAdmin):
    model = Ingredient


class PhotoAdmin(admin.StackedInline):
    model = Photo


class RecetteAdmin(admin.ModelAdmin):
    inlines = [ EtapeAdmin,IngredientAdmin,PhotoAdmin]


class IngredientAdmin(admin.ModelAdmin):
    inlines = [ IngredientAdmin2 ]


class TypeAdmin(admin.ModelAdmin):
    model = Type

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Ingredient, IngredientAdmin2)
