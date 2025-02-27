from django import forms

class TurmaForm(forms.Form):
   numero = forms.IntegerField(label='Número da Turma', required=True, help_text="Informe a turma do Aluno")
   horario_aula = forms.TimeField(label='Horário da Aula', required=True, help_text="Informe a hora em que a hora da aula da Turma")
   duracao_aula = forms.IntegerField(label='Duração da Aula', required=True), help_text="Informe a duração da aula da Turma"
   data_inicial = forms.DateField(label='Data Inicial', required=True, help_text="Informe a data inicial da Turma")
   data_final = forms.DateField(label='Data Final', required=False, help_text="Informe a data final da Turma")
   codigo_atividade = forms.IntegerField(label='Código da Atividade', required=True, help_text="Informe o código da atividade da Turma")
   matricula_monitor = forms.IntegerField(label='Matrícula do Monitor', required=False, help_text="Informe a matrícula do monitor da Turma")
   id_instrutor = forms.IntegerField(label='ID do Instrutor', required=True, help_text="Informe o ID do instrutor da Turma")
     