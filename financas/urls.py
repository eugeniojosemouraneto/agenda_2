from django.contrib import admin
from django.urls import path
from financas.views import *

app_name = 'financeiro'

urlpatterns = [
    path('', dashboad, name = 'dashboad'),
]
