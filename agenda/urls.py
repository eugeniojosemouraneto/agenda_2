from django.contrib import admin
from django.urls import path
from agenda.views import *

app_name = 'agenda'

urlpatterns = [
    path('tarefa/cadastro/', cadastro_tarefa, name = 'cadastro-tarefa'),
    path('tarefa/<int:id_tarefa>/alteracao/', alteracao_tarefa, name = 'alteracao-tarefa'),
    path('categoria/cadastro/', cadastro_categoria, name = 'cadastro-categoria'),
    path('tag/cadastro/', cadastro_tag, name = 'cadastro-tag'),
    path('cadastro/<int:id_tarefa>/descricao/', cadastro_descricao, name = 'cadastro-descricao'),
    path('cadastro/descricao/', cadastro_descricao, name = 'cadastro-descricao-form'),
    path('tarefa/<int:id_tarefa>/descricao/', descricao_tarefa, name = 'descricao'),
    path('tarefa/<int:id_tarefa>/deletar/', remover_tarefa, name = 'deletar'), # type: ignore
    path('tarefa/<int:id_tarefa>/concluida/', concluir_tarefa, name = 'concluir-tarefa'), # type: ignore
    path('ciclo/<int:id_ciclo>/descricao/', descricao_ciclo, name = 'descricao-ciclo'),
    path('ciclo/', home_ciclo, name = 'home-ciclo'),
    path('', home, name = 'home'),
]
