from datetime import datetime, date
from typing import Any
from django.db import models
from django.utils import timezone


class Financeiro(models.Model):

    class Meta:

        verbose_name = 'Financeiro'

    saldo = models.FloatField(default = 0.0)

    cofrinho = models.FloatField(default = 0.0)

    def saque_saldo(self, valor:float) -> bool:

        if self.saldo - valor >= 0.0:

            self.saldo -= valor

            return True
    
        return False
    
    def deposito_saldo(self, valor:float):

        self.saldo += valor

    def saque_cofrinho(self, valor:float) -> bool:

        if self.cofrinho - valor >= 0.0:

            self.cofrinho -= valor

            return True
        
        return False
    
    def deposito_cofrinho(self, valor:float):

        self.cofrinho += valor



class Categoria(models.Model):

    class Meta:

        verbose_name = 'Categoria'

        verbose_name_plural = 'Categorias'

    nome = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nome



class Locais(models.Model):

    class Meta:

        verbose_name = 'Local'

        verbose_name_plural = 'Locais'

    nome = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nome
    
    @classmethod
    def get_(cls, _local:str):

        return cls.objects.filter(nome = _local)





class Movimentacao_financeiro(models.Model):

    class Meta:

        verbose_name = 'Movimentação das finanças'

        verbose_name_plural = 'Movimentações das finanças'

        ordering = ['data', 'categoria', 'status']

    nome = models.CharField(max_length = 100)

    data = models.DateField()

    valor = models.FloatField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    mes = models.IntegerField()

    movimentacao = models.BooleanField()

    status = models.BooleanField()

    local = models.ForeignKey(
        Locais,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    def cofinho(self):

        self.mes = self.data.month

        if self.movimentacao:

            Financeiro.objects.get(pk = 0).deposito_cofrinho(self.valor)

        else:

            Financeiro.objects.get(pk = 0).saque_cofrinho(self.valor)

        self.save()

    def saldo(self):

        self.mes = self.data.month

        if self.movimentacao:

            Financeiro.objects.get(pk = 0).deposito_saldo(self.valor)

        else:

            Financeiro.objects.get(pk = 0).saque_saldo(self.valor)

        self.save()

    @classmethod
    def get_movimentacao_apagar(cls, _mes:int):

        return cls.objects.filter(
            mes = _mes
        )