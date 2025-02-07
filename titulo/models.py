from django.db import models
from django.urls import reverse

class Titulo(models.Model):
    
    codigo = models.AutoField(primary_key=True, 
                              help_text='Código do Titulo')
    descricao = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do Titulo')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'
