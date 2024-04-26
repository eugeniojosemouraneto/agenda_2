from django.shortcuts import render

def home(request):

    return render(
        request,
        'agenda/paginas/index.html',
    )