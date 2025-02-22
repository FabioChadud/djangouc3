from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType='html'><html><body><p>Olá, estou no App 'Tipo de Atividade'</p></body></html>")


def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()    
    contexto= {
        'tiposdeatividades': lista_tipodeatividade,
    }
    
    return render(request, 'tipodeatividade/listarTipoDeAtividade.html', context=contexto)
    
def detalhe_tipodeatividade(request, ta_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    return HttpResponse(tipodeatividade)