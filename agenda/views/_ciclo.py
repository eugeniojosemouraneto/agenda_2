from django.shortcuts import render, redirect, get_object_or_404
from agenda.constantes_app import *
from django.urls import reverse
from datetime import datetime
from agenda.models import *
from agenda.forms import *
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def home_ciclo(request):

    dia_hoje = datetime.now().strftime("%d/%m/%Y")

    ciclos = Ciclo.objects.all().filter()

    context = {
        'titulo'   : 'Ciclo de estudo',
        'dia_hoje' : f'{dia_hoje[0].upper() + dia_hoje[1:]}',
        'ciclos'   : ciclos,
    }

    return render(
        request,
        'agenda/paginas/ciclo/home_ciclo.html',
        context
    )

def descricao_ciclo(request, id_ciclo:int):

    dia_hoje = datetime.now().strftime("%d/%m/%Y")

    ciclo = get_object_or_404(
        Ciclo,
        pk = id_ciclo
    )

    categorias = Elemento_ciclo.get_categoria(id_ciclo)

    context = {
        'titulo'   : 'Ciclo ' + ciclo.nome,
        'dia_hoje' : f'{dia_hoje[0].upper() + dia_hoje[1:]}',
        'categorias' : categorias,
        'ciclo'    : ciclo,
    }

    return render(
        request,
        'agenda/paginas/ciclo/descricao_ciclo.html',
        context
    )