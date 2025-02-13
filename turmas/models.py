from django.db import models
from django.urls import reverse
from titulo.models import Titulo
from instrutores.models import Instrutores
from aluno.models import Aluno
from tipodeatividade.models import TipoDeAtividade 


class Turmas(models.Model):
    
    codigo = models.AutoField(primary_key=True, 
                              help_text='Código do Titulo')
    horarioaula = models.TimeField(max_length=70, null=False,
                                 help_text='Informe o horário da Aula:')
    duracaoaluna = models.DurationField(max_length=70, null=False,
                                 help_text='Informe a duração da Aula:')
    datainicial = models.DateField(max_length=70, null=False,
                                 help_text='Informe a data de Inicio:')
    datafinal = models.DateField(max_length=70, null=True, blank=True,
                                help_text='Informe a data de Término:')
    codigo_tipoatividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    codigo_instrutor = models.ForeignKey(Instrutores, on_delete=models.CASCADE)
    codigo_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.codigo