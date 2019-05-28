from django.shortcuts import render, redirect
from pools.models import *

# Create your views here.
def index(request):
    dados = {}
    dados['questions'] = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', dados)


def question(request, id):
    dados = {}
    dados['question'] = Question.objects.get(id=id)
    dados['choices'] = dados['question'].choices.all()
    return render(request, 'question.html', dados)


def result(request, id):
    dados = {}
    dados['question'] = Question.objects.get(id=id)
    dados['choices'] = dados['question'].choices.all()
    dados['total'] = calc_total(dados['choices'])

    votes_total = calc_total(dados['choices'])

    for choice in dados['choices']:
        if choice.votes == 0:
            choice.percent = 0
        else:
            percent = (choice.votes * 100) / votes_total
            choice.percent = '{0:.2f}'.format(percent)

    dados['choices'] = list(dados['choices'])
    dados['choices'].sort(key=lambda x: x.votes, reverse=True)

    return render(request, 'result.html', dados)


def vote(request, id):
    if request.method == 'POST':
        escolha = request.POST.get('choice')
        escolha = int(escolha)

        question = Question.objects.get(id=id)
        
        if not question.closed:
            choice = Choice.objects.get(id=escolha)
            choice.votes += 1
            choice.save()

            id = str(id)
            return redirect('/question/'+id+'/result')

    return redirect('/')


def calc_total(choices):
    result = 0
    for choice in choices:
        result += choice.votes
    return result
