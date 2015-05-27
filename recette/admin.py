from django.contrib import admin
from .models import Recette,  Ingredient,  Etape,  Photo, Note, Commentaire
from django.contrib.auth.models import User


class EtapeAdmin(admin.StackedInline):
    model = Etape

class NoteAdmin(admin.ModelAdmin):
    model = Note

class CommentaireAdmin(admin.ModelAdmin):
    model = Commentaire

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




admin.site.register(Recette, RecetteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Ingredient, IngredientAdmin2)
