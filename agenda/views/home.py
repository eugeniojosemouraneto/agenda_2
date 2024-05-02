from django.shortcuts import render, get_object_or_404
from agenda.constantes_app import *
from datetime import datetime
from agenda.models import *
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def home(request):
    dia_hoje = datetime.now().strftime("%d/%m/%Y")

    tarefas = Tarefa.atividades_do_mes(int(datetime.now().strftime("%m")))

    context = {
        'titulo'   : 'Agenda mensal',
        'pagina'   : 'mensal',
        'dia_hoje' : f'{dia_hoje[0].upper() + dia_hoje[1:]}',
        'tarefas'  : paginacao_geral(request, tarefas, 20),
    }

    return render(
        request,
        'agenda/paginas/index.html',
        context
    )

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