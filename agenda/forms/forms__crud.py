from bootstrap_datepicker_plus import widgets
from django.forms import ChoiceField, ModelForm
from agenda.models import *
from django import forms

class Categoria_form(ModelForm):

    class Meta:

        model = Categoria

        fields = (
            'nome',
        )

        widgets = {
            'nome' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Digite o nome da categoria',
                }
            )
        }

class Tarefa_form(ModelForm):

    class Meta:
    
        model = Tarefa
    
        fields = (
            'nome',
            'data',
            'categoria',
        )

        widgets = {
            'nome' : forms.TextInput(
                attrs = {
                    'class'       : 'form-control',
                    'placeholder' : 'Digite o nome da categoria',
                }
            ),
            'data': forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                },
                format = "%d/%m/%Y",
            ),
            'categoria' : forms.Select(
                attrs = {
                    'class' : 'form-select',
                },
            )
        }

class Tag_form(ModelForm):

    class Meta:

        model = Tag

        fields = (
            'nome',
            'cor'
        )

class Descricao_form(ModelForm):

    class Meta:

        model = Descricao

        fields = (
            'assunto',
            'tag',
        )