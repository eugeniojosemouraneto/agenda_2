# Generated by Django 5.0.4 on 2024-05-15 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_ciclo_descricao_alter_tarefa_hora'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarefa',
            options={'ordering': ['data', 'categoria', 'visibilidade'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data',
            field=models.DateField(default=datetime.date(2024, 5, 15)),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='hora',
            field=models.TimeField(default=datetime.time(21, 23, 18, 643448)),
        ),
    ]