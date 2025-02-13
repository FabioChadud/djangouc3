# Generated by Django 4.2.18 on 2025-02-12 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrutores', '0001_initial'),
        ('aluno', '0003_alter_aluno_matricula'),
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmas',
            name='codigo_aluno',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='codigo_intrutores',
        ),
        migrations.AddField(
            model_name='turmas',
            name='id',
            field=models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instrutores.instrutores'),
        ),
        migrations.AddField(
            model_name='turmas',
            name='matricula',
            field=models.ForeignKey(blank=True, db_column='matricula', null=True, on_delete=django.db.models.deletion.SET_NULL, to='aluno.aluno'),
        ),
    ]
