from django.shortcuts import render
from django.http import HttpResponse

from turma.models import Turma
from turma.forms import TurmaForm
# Create your views here.
def listar(request):
    lista_turma = Turma.objects.all()
    contexto = {
        'turmas':lista_turma
    }
    return render(request, 'turma/listarTurma.html', context=contexto)

def carregar_cadastro(request):
    lista_turma = Turma.objects.all()
    contexto = {
        'turmas':lista_turma
    }
    return render(request, 'turma/listarTurma.html', context=contexto)

def cadastrar(request):
    form = TurmaForm (request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data
        turma = Turma(descricao=dados_turma['descricao'])
        turma.save()
    
    lista_turma = Turma.objects.all()
    contexto = {
        'turmas':lista_turma
    }
    return render(request, 'turma/listarTurma.html', context=contexto)