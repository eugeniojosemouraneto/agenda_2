import project.constantes_app as constantes
from django.contrib import admin
from .models import *


@admin.register(Financeiro)
class Financeiro_admin(admin.ModelAdmin):

    list_display = 'saldo',  'cofrinho',

    list_per_page = constantes.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes.QUANT_PAGINAS_MAXIMAS



@admin.register(Categoria)
class Categoria_admin(admin.ModelAdmin):

    list_display = 'nome',

    list_per_page = constantes.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes.QUANT_PAGINAS_MAXIMAS



@admin.register(Locais)
class Locais_admin(admin.ModelAdmin):

    list_display = 'nome',

    list_per_page = constantes.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes.QUANT_PAGINAS_MAXIMAS



@admin.register(Movimentacao_financeiro)
class Movimentacao_financeiro_admin(admin.ModelAdmin):

    list_display = 'nome', 'data', 'valor', 'categoria', 'mes', 'movimentacao', 'local'

    ordering = 'data', 'categoria', 'movimentacao', 'local',

    list_filter = 'data', 'mes', 'categoria', 'movimentacao', 'local',

    list_editable = 'mes', 'categoria', 'movimentacao', 'local', 'valor' 

    list_display_links = 'nome', 

    search_fields = 'mes', 'data', 'categoria__nome', 'movimentacao', 'local__nome'
    # como categoria é uma chave estrangeira deve se determinar qual atributo da chave 
    # estrangeira que se quer fazer uma busca

    list_per_page = constantes.QUANT_DADOS_MAXIMOS_PAGINA

    list_max_show_all = constantes.QUANT_PAGINAS_MAXIMAS