from django.shortcuts import render
from django.http import HttpResponse
from aluno.models import Aluno

# Create your views here.
def index(request):
    return HttpResponse("<!DOCTYPE html><html><body><p>Olá, estou no App</p></body></html>")

def listar(request):
    lista_alunos = Aluno.objects.all()
    resposta = '<ul>'
    for aluno in lista_alunos:
        resposta += f'<li>{aluno.codigo} - {aluno.nome}</li>'
    resposta += '</ul>'
    return HttpResponse(resposta)

def consultar(request):
    return HttpResponse('Consultar')

def show_mensagem(request):
    x = 'M'
    nome = x + "arcos, tudo bem?"
    return HttpResponse(f'Bom dia! {nome}')