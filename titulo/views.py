from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return render(request, 'titulo/index.html')

def listar(request):
    lista_atividades = TipoDeAtividade.objects.all()
    return render(request, 'titulo/listar.html', {'lista_atividades': lista_atividades})

def show_mensagem(request):
    initial = 'M'
    nome = f"{x}arcos, tudo bem?"
    return HttpResponse(f'Bom dia! {nome}')