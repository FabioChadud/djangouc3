from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ("<DOCType ='html'><html><body><p>Olá, estou no App</p></body></html>")

def listar(request):
    return HttpResponse("Lista de Tipos de Atividade")

def consultar(request):
    return HttpResponse('Consultar')

def show_mensagem(request):
    x='M'
    nome=x+"arcos, tudo bem?"
    return HttpResponse('Bom dia!{nome}')

