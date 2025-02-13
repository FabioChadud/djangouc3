from django.shortcuts import render
from django.http import HttpResponse
from turmas.models import Turmas

# Create your views here.
def index(request):
    return render(request, 'turmas/index.html')

def listar(request):
    lista_atividades = Turmas.objects.all()
    return render(request, 'turmas/listar.html', {'lista_atividades': lista_atividades})

def show_mensagem(request):
    x = 'M'
    nome = x + "arcos, tudo bem?"
    return HttpResponse(f'Bom dia! {nome}')