from django.shortcuts import render
from django.http import HttpResponse

from titulo.models import Titulo

# Create your views here.

def listar(request):
    lista_titulo = Titulo.objects.all()    
    contexto= {
        'titulo': lista_titulo,
    }
    
    return render(request, 'titulo/listarTitulo.html', context=contexto)
    
def detalhe_titulo(request, ti_codigo):
    titulo = Titulo.objects.get(pk=ti_codigo)
    return HttpResponse(titulo)