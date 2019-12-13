#==============================================================
# CONSTRUYENDO FORMAS EN DJANGO
#==============================================================

from django import forms

from .models import Municipio

class FormularioAbogados(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea) 


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ('codigo_dane', 'departamento', 'municipio')  
