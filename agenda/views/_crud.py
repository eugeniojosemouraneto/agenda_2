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

def cadastro_categoria(request):

    form_action = reverse('agenda:cadastro-categoria')

    if request.method == 'POST':
    
        form = Categoria_form(request.POST)
    
        context = {
            'titulo'       : 'Cadastro de categoria',
            'form'         : form,
            'pagina'       : 'categoria',
            'form_action'  : form_action,
        }

        if form.is_valid():
    
            nova_categoria = form.save(commit = False)
    
            nova_categoria.save()
    
            return redirect('agenda:cadastro-tarefa')
        
        return render(
    
            request,
            'agenda/paginas/tarefa_form.html',
            context = context
        )
    
    context = {    
        'titulo'       : 'Cadastro de categoria',
        'pagina'       : 'categoria',
        'form'         : Categoria_form(),
    }

    return render(
        request,
        'agenda/paginas/tarefa_form.html',
        context = context
    )

def cadastro_tag(request):

    form_action = reverse('agenda:cadastro-tag')

    if request.method == 'POST':
    
        form = Tag_form(request.POST)
    
        context = {
            'titulo'       : 'Cadastro de tag',
            'form'         : form,
            'pagina'       : 'tag',
            'form_action'  : form_action,
        }

        if form.is_valid():
    
            nova_tag = form.save(commit = False)
    
            nova_tag.save()
    
            return redirect('agenda:cadastro-categoria')
        
        return render(
    
            request,
            'agenda/paginas/tarefa_form.html',
            context = context
        )
    
    context = {    
        'titulo'       : 'Cadastro de tag',
        'pagina'       : 'tag',
        'form'         : Tag_form(),
    }

    return render(
        request,
        'agenda/paginas/tarefa_form.html',
        context = context
    )

def cadastro_descricao(request, id_tarefa:int):

    form_action = reverse('agenda:cadastro-descricao-form')

    if request.method == 'POST':
    
        form = Descricao_form(request.POST)
    
        context = {
            'titulo'       : 'Cadastro de descrição',
            'form'         : form,
            'pagina'       : 'descricao',
            'form_action'  : form_action,
        }

        if form.is_valid():
    
            nova_descricao = form.save(commit = False)

            nova_descricao.tarefa = id_tarefa
    
            nova_descricao.save()
    
            return redirect('agenda:descricao', id_tarefa=id_tarefa)
        
        return render(
    
            request,
            'agenda/paginas/tarefa_form.html',
            context = context
        )
    
    context = {    
        'titulo'       : 'Cadastro de descrição',
        'pagina'       : 'descricao',
        'form'         : Descricao_form(),
    }

    return render(
        request,
        'agenda/paginas/tarefa_form.html',
        context = context
    )

def remover_tarefa(request, id_tarefa:int):

    tarefa = get_object_or_404(
        Tarefa.objects.filter(
            pk = id_tarefa,
            visibilidade = True
        ),
    )

    tarefa.deletar_tarefa()

    tarefa.save()

    return redirect('agenda:home')

def concluir_tarefa(request, id_tarefa:int):

    tarefa = get_object_or_404(
        Tarefa.objects.filter(
            pk = id_tarefa
        ),
    )

    tarefa.status = True

    tarefa.save()

    return redirect('agenda:descricao', id_tarefa)