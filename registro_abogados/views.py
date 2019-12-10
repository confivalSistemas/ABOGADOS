from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin # para que el usuario inicie sesion antes de ver el contenido

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

    # Numero de visitas de esta vista, contadas en la variable sesion
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'registro_abogados/index.html',
        context={'num_abogados':num_abogados,'num_municipios':num_municipios, 'num_visits':num_visits},
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

class AbogadosRegistradosView(LoginRequiredMixin, generic.ListView):
    model= DbAbogados
    context_object_name = 'abogados'
    #queryset = DbAbogados.objects.all()[:20]
    queryset = DbAbogados.objects.all()
    template_name = 'registro_abogados/abogados_list.html'
    paginate_by = 10

class AbogadoDetailView(generic.DetailView):
    model = DbAbogados
    template_name = 'registro_abogados/abogado_detail.html'
    context_object_name = 'abogado'
