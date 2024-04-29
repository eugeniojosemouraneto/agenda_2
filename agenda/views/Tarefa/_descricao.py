from django.shortcuts import render, get_object_or_404
from agenda.models import *


def descricao_tarefa(request, id_tarefa:int):

    tarefa = get_object_or_404(
        Tarefa.objects.filter(
            pk = id_tarefa,
            visibilidade = True
        ),
    )

    lembretes = Descricao.objects.all().filter(tarefa = id_tarefa)

    context = {
        'titulo'    : f'Descricao da tarefa {tarefa.nome}',
        'tarefa'    : tarefa,
        'lembretes' : lembretes,
    }

    return render(
        request,
        'agenda/paginas/tarefa.html',
        context
    )

