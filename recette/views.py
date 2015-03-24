from django.shortcuts import render

def index(request):
    contexte = {

    }
    return render(request, 'recette/index.html', contexte)

