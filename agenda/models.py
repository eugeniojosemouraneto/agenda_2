from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Categoria(models.Model):

    class Meta:

        verbose_name = 'Categoria'

        verbose_name_plural = 'Categorias'

    nome = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nome


class Tarefa(models.Model):
    
    class Meta:

        verbose_name = 'Tarefa'
    
        verbose_name_plural = 'Tarefas'

        ordering = ['data', 'categoria', 'visibilidade']

    nome = models.CharField(max_length = 100)

    data = models.DateField(default = timezone.now().date())

    mes = models.IntegerField(default = 0)

    hora = models.TimeField(default = timezone.now().time())

    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    visibilidade = models.BooleanField(default = True)

    status = models.BooleanField(default = False)

    @classmethod
    def atividades_do_mes(cls, _mes:int, visi:bool = True):
        
        return cls.objects.filter(
            visibilidade=visi,
            mes=_mes
        ).order_by('data', 'categoria')
    
    @classmethod
    def get_tarefa_categoria(cls, id_tarefa, visi:bool = True):

        return cls.objects.filter(
            visibilidade = visi,
            pk = id_tarefa
        ).order_by('categoria')
    
    
    def deletar_tarefa(self):

        self.visibilidade = False


class Conjunto_tarefa(models.Model):

    class Meta:

        verbose_name = 'Conjunto'

        verbose_name_plural = 'Conjuntos'

    nome = models.CharField(max_length = 100)

    id_tarefa = models.IntegerField()

    def __str__(self) -> str:
        
        return self.nome
    
    @classmethod
    def adicionar_tarefa(cls, id_tar:int, nome_conjunto:str):

        nova = cls(nome = nome_conjunto, id_tarefa = id_tar)

        nova.save()


class Tag(models.Model):

    class Meta:

        verbose_name = 'Tag'

        verbose_name_plural = 'Tags'

    nome = models.CharField(max_length = 100)

    cor = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.nome


class Descricao(models.Model):

    class Meta:

        verbose_name = 'Descrição'

        verbose_name_plural = 'Descrições'

        ordering = ['tag__nome', 'tag__cor']

    assunto = models.TextField()

    tag = models.ForeignKey(
        Tag,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    tarefa = models.IntegerField()

    def __str__(self) -> str:
        return self.tag.nome # type: ignore
    
    @classmethod
    def get_descricoes(cls, id_tarefa:int):
        
        return cls.objects.filter(
            tarefa = id_tarefa
        )


class Ciclo(models.Model):

    class Meta:

        verbose_name = 'Ciclo'

        verbose_name_plural = 'Ciclos'

    nome = models.CharField(max_length = 100)

    descricao = models.TextField(default = "")

    tempo_disponivel_semana = models.IntegerField(default = 1)

    def __str__(self) -> str:
        
        return self.nome
    
    @classmethod
    def reiniciar_ciclo(cls, id_ciclo:int):

        elementos = Elemento_ciclo.objects.all().filter(ciclo = id_ciclo)

        for elem in elementos:

            elem.horas_cumpridas = 0

            elem.save()


class Elemento_ciclo(models.Model):

    class Meta:

        verbose_name = 'Elemento de ciclo'

        verbose_name_plural = 'Elementos de clico'

        ordering = ['categoria__nome', 'ciclo__pk']

    horas_categoria = models.IntegerField(default = 0)

    horas_cumpridas = models.IntegerField(default = 0)

    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    dificuldade = models.IntegerField(default = 1)

    ciclo = models.ForeignKey(
        Ciclo,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    @classmethod
    def get_categoria(cls, id_ciclo:int):

        return cls.objects.filter(
            ciclo = id_ciclo
        )