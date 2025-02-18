from django.utils import timezone
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

class TurmaAluno(models.Model):
    id_turma = models.ForeignKey(Turmas, on_delete=models.CASCADE,
                                 help_text="Número da Turma do Aluno.")
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,
                                 help_text="Número da matrícula do Aluno.")
    data_inicio_maricula = models.DateField(null=False, 
                                            default=timezone.now(), 
                                            help_text='Informe a data de Inicio da Matrícula:')
    data_fim_matricula = models.DateField(null=True, blank=True,
                                          help_text='Informe a data de Término da Matrícula:')
    
    def __str__(self):
        resposta = f'Turma: {self.id} - Aluno: {self.matricula_aluno}'
        return resposta

class Ausencia(models.Model):
    id_turma = models.ForeignKey(Turmas, on_delete=models.CASCADE,
                                 help_text="Número da Turma do Aluno.")
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,
                                 help_text="Número da matrícula do Aluno.")
    data_ausencia = models.DateField(null=False,
                                     default=timezone.now(),
                                     help_text='Informe a data da Ausência:')
    justificativa = models.CharField(max_length=200, null=False,
                                     help_text='Informe a Justificativa da Ausência:')
    
    def __str__(self):
        resposta = f'Turma: {self.id} - Aluno: {self.matricula_aluno} - Data da Ausência: {self.data_ausencia}'
        return resposta