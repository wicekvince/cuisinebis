from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Reponse


class IndexView(generic.ListView):
    model = Question
    template_name = 'sondages/index.html'
    context_object_name = 'questions'


def index(request):
    contexte = {
        'questions': Question.objects.all(),
    }
    return render(request, 'sondages/index.html', contexte)


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    contexte = {
        'question': question,
    }
    return render(request, 'sondages/detail.html', contexte)


def resultats(request, id):
    question = get_object_or_404(Question, id=id)
    contexte = {
        'question': question,

    }
    return render(request, 'sondages/resultats.html', contexte)


def voter(request):
    if (request.method == 'POST'):
        id_reponse = request.POST['vote']
        reponse = Reponse.objects.get(id=id_reponse)
        reponse.score += 1
        reponse.save()
        return redirect('sondages:resultats', reponse.question_id)
    return redirect('sondages:index')


def test(request):
    from .forms import ReponseForm
    if request.method == 'POST':
        formulaire = ReponseForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = ReponseForm
    contexte = {
        'formulaire': formulaire,
    }
    return render(request, 'sondages/test.html', contexte)