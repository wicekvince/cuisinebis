from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ingredient,  Etape,  Photo,  Recette


def index(request):
    contexte = {

    }
    return render(request, 'recette/index.html', contexte)


def register(request):
    if (request.method == 'POST'):
        user_form = UserCreationForm(request.POST    )
        if user_form.is_valid():
            user = User.objects.create_user(request.POST['username'],'',request.POST['password1'])
            user.save()
            return redirect('recette:index')
    else:
        user_form = UserCreationForm()
    contexte = {
        'formulaire': user_form,
    }
    return render(request, 'registration/register.html', contexte)

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
