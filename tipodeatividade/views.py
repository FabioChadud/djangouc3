from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar(request):
    lista_atividades = TipoDeAtividade.objects.all()
    resposta = ['<ul>']
    for atividade in lista_atividades:
        resposta.append(f'<li>{atividade.codigo} - {atividade.descricao}</li>')
    resposta.append('</ul>')
    resposta = ''.join(str(item) for item in resposta)
    return HttpResponse(resposta)

def consultar(request):
    return HttpResponse('Consultar')
def show_mensagem(request):
    initial_letter = 'M'
    nome = initial_letter + "arcos, tudo bem?"
    return HttpResponse(f'Bom dia! {nome}')