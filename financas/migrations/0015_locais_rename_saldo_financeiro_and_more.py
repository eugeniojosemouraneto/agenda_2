# Generated by Django 5.0.4 on 2024-05-15 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0014_alter_movimentacao_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.RenameModel(
            old_name='Saldo',
            new_name='Financeiro',
        ),
        migrations.AlterModelOptions(
            name='financeiro',
            options={'verbose_name': 'Financeiro'},
        ),
        migrations.CreateModel(
            name='Movimentacao_financeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('valor', models.FloatField()),
                ('mes', models.IntegerField()),
                ('movimentacao', models.BooleanField()),
                ('status', models.BooleanField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financas.categoria')),
                ('local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financas.locais')),
            ],
            options={
                'verbose_name': 'Movimentação das finanças',
                'verbose_name_plural': 'Movimentações das finanças',
                'ordering': ['data', 'categoria', 'status'],
            },
        ),
        migrations.DeleteModel(
            name='Movimentacao',
        ),
    ]
