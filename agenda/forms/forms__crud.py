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
                    'class' : 'texto form-control',
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
            'mes',
        )

        widgets = {
            'nome' : forms.TextInput(
                attrs = {
                    'class'       : 'texto form-control',
                    'placeholder' : 'Digite o nome da categoria',
                }
            ),
            'data': forms.DateInput(
                attrs = {
                    'class' : 'texto form-control',
                },
                format = "%d/%m/%Y",
            ),
            'categoria' : forms.Select(
                attrs = {
                    'class' : 'texto form-select',
                },
            ),
            'mes' : forms.NumberInput(
                attrs = {
                    'class' : 'texto form-control', 
                }
            ),
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

class Ciclo_form(ModelForm):

    class Meta:

        model = Ciclo

        fields = (
            'nome',
            'tempo_disponivel_semana',
        )

        widgets = {
            'nome' : forms.TextInput(
                attrs = {
                    'class'       : 'texto form-control',
                    'placeholder' : 'Digite o nome da categoria',
                }
            ),
            'tempo_disponivel_semana' : forms.NumberInput(
                attrs = {
                    'class' : 'texto form-control',
                    'placeholder' : 'Digite a quantidade de horas disponivel na sua semana.',
                }
            )
        }


class Elemento_ciclo_form(ModelForm):

    class Meta:

        model = Elemento_ciclo

        fields = (
            'horas_categoria',
            'categoria',
            'dificuldade',
        )

        widgets = {
            'horas_categoria' : forms.NumberInput(
                attrs = {
                    'class'       : 'form-control',
                }
            ),
            'categoria' : forms.Select(
                attrs = {
                    'class' : 'form-select',
                },
            ),
            'dificuldade' : forms.NumberInput(
                attrs = {
                    'class'       : 'form-control',
                }
            ),
        }