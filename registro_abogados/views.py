from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django import forms

#========================================================================================================================================
#==> configuraciones para validacion
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

#aca se tienen que llamar a los modelos
from .models import DbAbogados

# Create your views here.

#========================================================================================================================================
#==> Aqui se hace la primera configuracion de vistas

# def index(request):
#     return HttpResponse("BIENVENIDO AL REGISTRO DE ABOGADOS DE CONFIVAL")

# def registro(request):
#     latest_abogado_list = DbAbogados.objects.order_by('codigo')
#     template = loader.get_template('registro_abogados/prueba_register.html')
#     context = {
#         'latest_abogado_list': latest_abogado_list,
#     }
#     return HttpResponse(template.render(context, request))  

#=========================================================================================================================================
#==> Aqui se hace la configuracion personalizada de vistas

class RegistroView(generic.ListView):
    template_name = 'registro_abogados/db_abogados.html'
    context_object_name = 'latest_abogado_list'

    def get_queryset(self):
        return DbAbogados.objects.order_by('codigo')

class FormularioView(generic.ListView):
    template_name = 'registro_abogados/formularios.html'
    context_object_name = 'latest_abogado_list'

    def get_queryset(self):
        return DbAbogados.objects.order_by('codigo')

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    

