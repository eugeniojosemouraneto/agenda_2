# -------------------------------------------------------------------------------------------------------------------------------------------------------
#    Admin
# 
QUANT_DADOS_MAXIMOS_PAGINA = 30
QUANT_PAGINAS_MAXIMAS = 200000
# 
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#   Constantes uteis
def paginacao_geral(request, elementos_paginado, num_max_elem_pagina:int):

    from django.core.paginator import Paginator

    paginacao = Paginator(elementos_paginado, num_max_elem_pagina)

    pagina_numero = request.GET.get('page')

    return paginacao.get_page(pagina_numero)