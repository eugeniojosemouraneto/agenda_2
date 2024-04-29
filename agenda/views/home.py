from django.shortcuts import render
from datetime import datetime
from agenda.models import *
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def home(request):
    dia_hoje = datetime.now().strftime("%A, %d/%m/%Y")

    tarefas = Tarefa.atividades_do_mes(int(datetime.now().strftime("%m")))

    context = {
        'titulo'   : 'Agenda menssal',
        'dia_hoje' : f'{dia_hoje[0].upper() + dia_hoje[1:]}',
        'tarefas'  : tarefas,
    }

    return render(
        request,
        'agenda/paginas/index.html',
        context
    )

