from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar(request):
    from django.core.paginator import Paginator
    resposta = ['<ul>']
    for atividade in lista_atividades:
        resposta.append('<li>{} - {}</li>'.format(atividade.codigo, atividade.descricao))
    resposta.append('</ul>')
    resposta = ''.join(resposta)
    resposta_list = ['<ul>']
    for atividade in page_obj:
        resposta_list.append(f'<li>{atividade.codigo} - {atividade.descricao}</li>')
    resposta_list.append('</ul>')
    resposta_str = ''.join(str(item) for item in resposta_list)
    return HttpResponse(resposta_str)

def consultar(request):
    return HttpResponse('Consultar')
def show_mensagem(request):
    initial_letter = 'M'
    nome = initial_letter + "arcos, tudo bem?"
    return HttpResponse(f'Bom dia! {nome}')

from django.http import Http404

def detalhe_tipodeatividade(request, ta_codigo):
    try:
        tipo_de_atividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    except TipoDeAtividade.DoesNotExist:
        raise Http404("Tipo de Atividade does not exist")
    return HttpResponse(tipo_de_atividade)