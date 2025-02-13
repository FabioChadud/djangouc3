from django.db import models
from django.urls import reverse

from titulo.models import Titulo

class Instrutores(models.Model):
    
    codigo = models.AutoField(primary_key=True, 
                              help_text='ID do Instrutor')
    rg = models.CharField(max_length=70, null=False,
                                 help_text='rg do Instrutor')
    nome = models.CharField(max_length=70, null=False,
                                 help_text='nome do Instrutor')
    data_nascimento = models.DateField(max_length=70, null=True, blank=True,
                                 help_text='data de nascimento do Instrutor')
    telefone = models.CharField(max_length=70, null=False,
                                 help_text='telefone do Instrutor')
    ddd = models.CharField(max_length=70, null=False,
                                 help_text='ddd do Instrutor')
    codigo_titulo = models.ForeignKey(Titulo, on_delete=models.SET_NULL, null=True, blank=True, db_column='codigo_titulo',)
    
    def __str__(self):
        return self.codigo