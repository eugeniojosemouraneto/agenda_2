from datetime import datetime, date
from django.db import models
from django.utils import timezone


class Categoria(models.Model):

    class Meta:

        verbose_name = 'Categoria'

        verbose_name_plural = 'Categorias'

    nome = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nome
    

class Movimentacao(models.Model):

    class Meta:

        verbose_name = 'Movimentacao'

        verbose_name_plural = 'Movimentacoes'

        ordering = ['nome', 'data', 'categoria', 'pk']

    nome = models.CharField(max_length = 100)

    hora = models.TimeField(default = timezone.now().time())

    data = models.DateField(default = timezone.now().date())
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    visibilidade = models.BooleanField(default = True)


class Saldo(models.Model):
    
    class Meta:

        verbose_name = 'Saldo'
    
    saldo = models.FloatField(default = 0.00)

    cofrinho = models.FloatField(default = 0.00)

    def possivel_saque_saldo(self, valor_retirado:int) -> bool:
        
        if(self.saldo - valor_retirado >= 0.00):

            return True
        
        return False
    
    def possivel_saque_cofrinho(self, valor:int) -> bool:

        if self.cofrinho - valor >= 0.00:

            return True
        
        return False

    def saque_saldo(self, valor_retirado:int):

        if self.possivel_saque_saldo(valor_retirado):

            self.saldo -= valor_retirado

    def saque_cofrinho(self, valor:int):

        if self.possivel_saque_cofrinho:
        
            self.cofrinho -= valor

    def deposito_saldo(self, valor:int):

        self.saldo += valor

    def deposito_cofrinho(self, valor:int):

        self.cofrinho += valor    