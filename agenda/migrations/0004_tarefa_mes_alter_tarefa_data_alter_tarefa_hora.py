# Generated by Django 5.0.4 on 2024-05-01 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_tarefa_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data',
            field=models.DateField(default=datetime.date(2024, 5, 1)),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='hora',
            field=models.TimeField(default=datetime.time(18, 38, 14, 741988)),
        ),
    ]