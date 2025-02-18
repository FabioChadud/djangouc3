from django.contrib import admin
from .models import Turmas, Ausencia, TurmaAluno

admin.site.register(Turmas)
admin.site.register(TurmaAluno)
admin.site.register(Ausencia) 