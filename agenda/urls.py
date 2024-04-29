from django.contrib import admin
from django.urls import path
from agenda.views import *

app_name = 'agenda'

urlpatterns = [
    path('descricao/tarefa/<int:id_tarefa>/', descricao_tarefa, name = 'descricao'),
    path('', home, name = 'home'),
]
