# Generated by Django 5.0.4 on 2024-04-28 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0009_alter_movimentacao_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='hora',
            field=models.TimeField(default=datetime.time(22, 43, 53, 208292)),
        ),
    ]