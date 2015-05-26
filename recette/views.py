from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RecetteForm,EtapeForm,RegistrationForm
from .models import Ingredient,  Etape,  Photo,  Recette
from django import template
import pprint

def index(request):
    recettes = Recette.objects.all()
    contexte = {
        'recettes': recettes,
    }
    return render(request, 'recette/index.html', contexte)


def register(request):
    if (request.method == 'POST'):
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password1'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return redirect('recette:index')
    else:
        user_form = RegistrationForm()
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

def nouvelleRecette(request):

    if request.method == "POST":
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form = RecetteForm()

    from django.forms.models import inlineformset_factory
    BookFormSet = inlineformset_factory(Recette, Etape, RecetteForm)
    formset = BookFormSet
    BookFormSet2 = inlineformset_factory(Recette, Ingredient, RecetteForm)
    formset2 = BookFormSet2
    form3 = RecetteForm
    contexte = {
        'form'    : formset,
        'form2'    : formset2,
        'form3'    : form3,
    }
    return render(request, 'recette/nouvelle-recette.html', contexte)

def search(request):
    query = request.GET.get('search_query')
    if request.GET.get('orderby') and request.GET.get('orderway'):
        orderby = request.GET.get('orderby')
        orderway = request.GET.get('orderway')
        if orderway == 'desc':
            results = Recette.objects.filter(titre__contains=query).order_by('-' + orderby).select_related()
        elif orderway == 'asc':
            results = Recette.objects.filter(titre__contains=query).order_by(orderby).select_related()
    else :
        results = Recette.objects.filter(titre__contains=query).select_related()
    contexte = {
        'query': query,
        'results' : results
    }
    return render(request, 'search/search_result.html', contexte)