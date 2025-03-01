from django.shortcuts import render
from django.http import HttpResponse

from aluno.models import Aluno
from aluno.forms import AlunoForm

# Create your views here.
def listar(request):
    lista_aluno = Aluno.objects.all()
    contexto = {
        'alunos': lista_aluno,
    }
    
    return render(request, 'aluno/listarAluno.html', context=contexto)

def carregar_cadastro(request):
    lista_aluno =  Aluno.objects.all()
    context = {
        'aluno':lista_aluno
    }
    return render(request, 'aluno/cadastrarAluno.html')

def cadastrar(request):
    form = AlunoForm (request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        aluno = Aluno(
            id = dados_instrutor['id'],
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            data_nascimento = dados_instrutor['data_nascimento'],
            telefone = dados_instrutor['telefone'],
            ddd = dados_instrutor['ddd'],
            codigo_titulo = dados_instrutor['codigo_titulo'],
            )
            
        aluno.save()
    return render(request, 'aluno/cadastrarAluno.html')