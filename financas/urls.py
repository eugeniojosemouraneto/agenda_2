from django.contrib import admin
from django.urls import path
from agenda.views import *

app_name = 'financas'

urlpatterns = [
    path('', home, name = 'home'),
]
