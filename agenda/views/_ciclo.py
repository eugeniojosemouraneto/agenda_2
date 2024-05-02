from django.shortcuts import render, redirect, get_object_or_404
from agenda.constantes_app import *
from django.urls import reverse
from datetime import datetime
from agenda.models import *
from agenda.forms import *
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def cadastro_tarefa(request):

    form_action = reverse('agenda:cadastro-tarefa')
    
    categorias = Categoria.objects.all().filter()

    if request.method == 'POST':
    
        form = Tarefa_form(request.POST)
    
        context = {
            'titulo'       : 'Cadastro de tarefa',
            'categorias'   : categorias,
            'form'         : form,
            'pagina'       : 'tarefa',
            'form_action'  : form_action,
        }

        if form.is_valid():
    
            nova_tarefa = form.save(commit = False)
    
            nova_tarefa.save()
    
            return redirect('agenda:descricao', nova_tarefa.pk)
        
        return render(
    
            request,
            'agenda/paginas/tarefa_form.html',
            context = context
        )
    
    context = {    
        'titulo'       : 'Cadastro de tarefa',
        'categorias'   : categorias,
        'pagina'       : 'tarefa',
        'form'         : Tarefa_form(),
    }

    return render(
        request,
        'agenda/paginas/tarefa_form.html',
        context = context
    )
