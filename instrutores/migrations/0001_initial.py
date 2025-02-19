# Generated by Django 4.2.18 on 2025-02-11 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutores',
            fields=[
                ('id', models.AutoField(help_text='ID do Instrutor', primary_key=True, serialize=False)),
                ('rg', models.CharField(help_text='rg do Instrutor', max_length=70)),
                ('nome', models.CharField(help_text='nome do Instrutor', max_length=70)),
                ('data_nascimento', models.DateField(blank=True, help_text='data de nascimento do Instrutor', max_length=70, null=True)),
                ('telefone', models.CharField(help_text='telefone do Instrutor', max_length=70)),
                ('ddd', models.CharField(help_text='ddd do Instrutor', max_length=70)),
                ('codigo_titulo', models.ForeignKey(blank=True, db_column='codigo_titulo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='titulo.titulo')),
            ],
        ),
    ]
