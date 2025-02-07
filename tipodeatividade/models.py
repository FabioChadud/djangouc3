from django.db import models
from django.urls import reverse

class TipoDeAtividade(models.Model):
    
    codigo = models.AutoField(primary_key=True, 
                              help_text='Código do Tipo de atividade')
    descricao = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do Tipo de Atividade')
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'