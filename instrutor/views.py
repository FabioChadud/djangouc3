from django.shortcuts import render
from django.http import HttpResponse

from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    return HttpResponse(lista_instrutor)

def carregar_cadastro(request):
    return render(request, 'instrutor/cadastrarInstrutor.html')

def cadastrar(request):
    form = InstrutorForm (request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(descricao=dados_instrutor['descricao'])
        instrutor.save()
    return render(request, 'instrutor/cadastrarInstrutor.html')