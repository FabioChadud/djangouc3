from django.shortcuts import render
from django.http import HttpResponse
from titulo.models import Titulo
from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores':lista_instrutor
    }
    return render(request, 'instrutor/listarInstrutor.html', context=contexto)

def carregar_cadastro(request):
    lista_titulo =  Titulo.objects.all()
    contexto = {
        'titulos':lista_titulo
    }
    return render(request, 'instrutor/cadastrarInstrutor.html', context=contexto)

def cadastrar(request):
    form = InstrutorForm (request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        #Recuperando o objeto título com a chave priméria informada no formulário instrutor.
        titulo = Titulo.objects.get(pk=dados_instrutor['codigo_titulo'])
        instrutor = Instrutor(
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            data_nascimento = dados_instrutor['data_nascimento'],
            telefone = dados_instrutor['telefone'],
            ddd = dados_instrutor['ddd'],
            codigo_titulo = titulo
            )
            
        instrutor.save()
        
    lista_titulo =  Titulo.objects.all()
    contexto = {
        'titulo':lista_titulo
    }
    return render(request, 'instrutor/cadastrarInstrutor.html', context=contexto)