from django.db import models
from django.urls import reverse
from django.utils import timezone
from titulo.models import Titulo
from aluno.models import Aluno
from tipodeatividade.models import TipoDeAtividade 


class Instrutores(models.Model):
    
    id = models.AutoField(primary_key=True)
    rg = models.CharField(max_length=15, help_text="Informe o RG do Instrutor")
    nome = models.CharField(max_length=70, help_text="Informe o nome do Instrutor")
    dataNascimento = models.DateField(null=True, blank=True, help_text="Informe a data de nascimento do Instrutor")
    telefone = models.CharField(max_length=9, help_text="Informe o telefone do Instrutor")
    ddd = models.CharField(max_length=3, help_text="Informe o DDD do telefone do Instrutor")
    codigo_titulo = models.ForeignKey(Titulo, null=True, blank=True, on_delete=models.SET_NULL, db_column="titulo_codigo")
    
    def _str_(self):
        return f'{self.id} - {self.nome}'    
        
    def __str__(self):
        return str(self.codigo)