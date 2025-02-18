from django.shortcuts import render
from django.http import HttpResponse
from turmas.models import Turmas

# Create your views here.
def index(request):
    return render(request, 'escola.html')

def listar(request):
    lista_turma = Turmas.objects.all()
    return HttpResponse(lista_turma)
