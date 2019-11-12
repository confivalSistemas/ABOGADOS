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
from .models import DbAbogados, Municipio, Genero

# Create your views here.

#========================================================================================================================================
#==> Aqui se hace la primera configuracion de vistas
def index(request):
    """
    Funcion vista para la pagina de inicio
    """
    # Genera contadores de algunos de los objetos principales
    num_abogados =DbAbogados.objects.all().count()
    num_municipios = Municipio.objects.all().count()   
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'registro_abogados/index.html',
        context={'num_abogados':num_abogados,'num_municipios':num_municipios},
    )
        

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