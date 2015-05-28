from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RecetteForm,EtapeForm,RegistrationForm,IngredientForm, CommentaireForm, NoteForm
from .models import Ingredient,  Etape,  Photo,  Recette, Note, Commentaire, Type
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pprint
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from django.db.models import Avg

TYPE_CHOICES = ['1','2','3','4'];

def index(request):

    recettes = Recette.objects.all();
    nb = recettes.count()
    typeObjet=None
    if request.method == 'GET':
        if request.GET.get('type'):
            if request.GET['type'] in TYPE_CHOICES:
                type = request.GET['type']
                typeObjet = Type.objects.get(id=type)
                recettes = Recette.objects.filter(type=type);

    contexte = {
        'typeObjet': typeObjet,
        'recettes': recettes,
        'nb' : nb

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

    if (request.method == 'POST'):
        com_form = CommentaireForm(request.POST)
        note_form = NoteForm(request.POST)
        #add default user and recette TODO
        note_form.user = 1
        note_form.recette = id
        com_form.user = 1
        com_form.recette = id
        if com_form.is_valid():
            com_form.save()
        if note_form.is_valid():
            note_form.save()


    recette = Recette.objects.get(id=id)
    etapes = Etape.objects.filter(recette=id)
    ingredients = Ingredient.objects.filter(recette=id)
    photos = Photo.objects.filter(recette=id)
    note = Note.objects.filter(recette=id).aggregate(Avg('note'))
    noted = Note.objects.filter(recette=id).count()
    form_note = ''
    if noted == 0:
        form_note = NoteForm();
    commentaires = Commentaire.objects.filter(recette=id)
    form_com = CommentaireForm();
    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'photos'     : photos,
        'note'     : note,
        'commentaires'     : commentaires,
        'form_note': form_note,
        'form_com': form_com,
    }
    return render(request, 'recette/affiche-recette.html', contexte)

def nouvelleRecette(request):

    if request.method == "POST":
        form = RecetteForm(request.POST)
        formEtape = EtapeForm(request.POST)
        formRecette = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
        if formEtape.is_valid():
            formEtape.save()
        if formRecette.is_valid():
            formRecette.save()

    recette = Recette.objects.get(id=1)


    form = RecetteForm(instance=recette);
    EtapeFormSet = inlineformset_factory(Recette,Etape,EtapeForm)
    IngredientFormSet2 = inlineformset_factory(Recette,Ingredient, RecetteForm)


    contexte = {
        'form'    : form,
        'form2'    : EtapeFormSet,
        'form3'    : IngredientFormSet2,
    }
    return render(request, 'recette/nouvelle-recette.html', contexte)


def supprimerRecette(request, id):
    suppr = Recette.objects.get(id=id).delete()
    return render(request, 'recette/mes_recettes.html')

def search(request):

    query = request.GET.get('search_query')
    orderby = ''
    orderway = ''
    if request.GET.get('orderby') and request.GET.get('orderway'):
        orderby = request.GET.get('orderby')
        orderway = request.GET.get('orderway')
        if orderway == 'desc':
            results = Recette.objects.filter(titre__contains=query).order_by('-' + orderby).select_related()
        elif orderway == 'asc':
            results = Recette.objects.filter(titre__contains=query).order_by(orderby).select_related()
    else :
        results = Recette.objects.filter(titre__contains=query).select_related()
    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)
    contexte = {
        'page': page,
        'orderby': orderby,
        'orderway': orderway,
           'query': query,
        'results' : results
    }
    return render(request, 'search/search_result.html', contexte)

def mes_recettes(request):
    results = None;
    if request.user.is_authenticated():
        results = Recette.objects.filter(user_id=request.user.id)
    contexte = {
        'results': results
    }
    return render(request, 'recette/mes_recettes.html', contexte)