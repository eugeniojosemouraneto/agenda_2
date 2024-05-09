from django.contrib import admin

import agenda.constantes_app as constantes_aplicacao
from agenda.models import *


@admin.register(Categoria)
class Categoria_admin(admin.ModelAdmin):
    
    list_display = 'nome',
    
    ordering = 'id',

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS

@admin.register(Tarefa)
class Tarefa_admin(admin.ModelAdmin):
    
    list_display = 'nome',  'id', 'data', 'categoria', 'visibilidade',
    
    ordering = 'data', 'categoria', 'nome', 'visibilidade',

    list_filter = 'data', 'hora', 'categoria', 'visibilidade', 

    list_editable = 'visibilidade', 

    list_display_links = 'nome', 'categoria',

    search_fields = 'nome', 'data', 'categoria__nome',
    # como categoria é uma chave estrangeira deve se determinar qual atributo da chave 
    # estrangeira que se quer fazer uma busca

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS



@admin.register(Conjunto_tarefa)
class Conjunto_tarefa_admin(admin.ModelAdmin):
    
    list_display = 'nome', 'id_tarefa', 'pk',
    
    ordering = 'id', 'nome', 

    search_fields = 'nome', 'id_tarefa',

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS


@admin.register(Tag)
class Tag_admin(admin.ModelAdmin):

    list_display = 'nome', 'cor',

    search_fields = 'nome', 

    list_editable = 'cor',

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS   

@admin.register(Descricao)
class Descricao_admin(admin.ModelAdmin):

    list_display = 'assunto', 'tag', 'tarefa',

    search_fields = 'tag__nome',

    list_filter = 'tag__nome', 

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS


@admin.register(Ciclo)
class Ciclo_admin(admin.ModelAdmin):

    list_display = 'nome', 'tempo_disponivel_semana',

    search_fields = 'nome',

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS


@admin.register(Elemento_ciclo)
class Elemento_ciclo_admin(admin.ModelAdmin):

    list_display = 'ciclo', 'horas_categoria', 'horas_cumpridas', 'categoria', 'dificuldade', 

    search_fields = 'categoria', 'ciclo',

    list_filter = 'categoria', 'ciclo',

    list_per_page = constantes_aplicacao.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes_aplicacao.QUANT_PAGINAS_MAXIMAS