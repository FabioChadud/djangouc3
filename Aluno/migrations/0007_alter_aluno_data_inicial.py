# Generated by Django 4.2.18 on 2025-02-13 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0006_alter_aluno_data_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 13, 0, 36, 21, 122086, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial de matrícula do Aluno'),
        ),
    ]
