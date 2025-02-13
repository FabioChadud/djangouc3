from django.db import models
from django.urls import reverse

class Aluno(models.Model):
    
    codigo = models.AutoField(primary_key=True, 
                              help_text='Matricula do Aluno')
    nome = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do Aluno')
    datainicial = models.DateField(max_length=70, null=True,blank=True,
                                 help_text='Informe a data inicial do Aluno')
    datafinal = models.DateField(max_length=70, null=True,blank=True,
                                 help_text='Informe a data final do Aluno')
    def __str__(self):
        return self.nome
