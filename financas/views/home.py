from django.shortcuts import render

def home(request):

    context = {
        'pagina' : 'financeiro',
        'titulo' : 'Finanças'
    }

    return render(
        request,
        'financas/paginas/index.html',
        context
    )