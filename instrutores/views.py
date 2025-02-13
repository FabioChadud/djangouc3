from django.shortcuts import render
from django.http import HttpResponse
from instrutores.models import Instrutores

# Create your views here.
def index(request):
    return render(request, 'instrutores/index.html')

def listar(request):
    lista_instrutores = Instrutores.objects.all()
    return render(request, 'instrutores/listar.html', {'instrutores': lista_instrutores})

def show_mensagem(request):
    return HttpResponse('Bom dia!')