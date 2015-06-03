from django.contrib import admin
from .models import Recette,  Ingredient,  Etape,  Photo, Note, Commentaire, Type, Difficulte


class EtapeAdmin(admin.StackedInline):
    model = Etape


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ('note','recette','user')
    list_display_links = ('note','recette','user')


class CommentaireAdmin(admin.ModelAdmin):
    model = Commentaire
    list_display = ('message','recette','user')
    list_display_links = ('message','recette','user')


class IngredientAdmin(admin.StackedInline):
    model = Ingredient


class IngredientAdmin2(admin.ModelAdmin):
    model = Ingredient
    list_display = ('nom','quantite')
    list_display_links = ('nom','quantite')


class PhotoAdmin(admin.StackedInline):
    model = Photo


class RecetteAdmin(admin.ModelAdmin):
    inlines = [ EtapeAdmin,IngredientAdmin,PhotoAdmin ]
    list_display = ('titre','user')
    list_display_links = ('titre','user')


class IngredientAdmin(admin.ModelAdmin):
    inlines = [ IngredientAdmin2 ]


class TypeAdmin(admin.ModelAdmin):
    model = Type


class DifficulteAdmin(admin.ModelAdmin):
    model = Difficulte

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Difficulte, DifficulteAdmin)
admin.site.register(Ingredient, IngredientAdmin2)
