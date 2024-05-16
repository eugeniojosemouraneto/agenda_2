from django.shortcuts import render
from ..models import *

def dashboad(request):

    data = datetime.now().strftime("%d/%m/%Y")
    mes = datetime.now().month

    return render(
        request,
        'financas/paginas/index.html',
        {
            'titulo'        : 'Finanças',
            'dia'           : data,
            'movimentation' : Movimentacao_financeiro.get_movimentacao_apagar(mes),
            'financeiro'    : Financeiro.objects.get(pk = 1),
        }
    )