#==============================================================
# CONSTRUYENDO FORMAS EN DJANGO
#==============================================================

from django import forms

class FormularioAbogados(forms.Form):
    your_name = forms.CharField(label='Tu nombre', max_length=100)

    