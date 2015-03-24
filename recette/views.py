from django.shortcuts import render
from .models import Recette,Ingredient,Etape,Photo

def index(request):
    contexte = {

    }
    return render(request, 'recette/index.html', contexte)

def recette(request, id):
    recette = Recette.objects.get(id=id)
    etapes = Etape.objects.filter(recette=id)
    ingredients = Ingredient.objects.filter(recette=id)
    photos = Photo.objects.filter(recette=id)
    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'photos'     : photos,
    }
    return render(request, 'recette/affiche-recette.html', contexte)
