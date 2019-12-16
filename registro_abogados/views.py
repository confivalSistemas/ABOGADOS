from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin # para que el usuario inicie sesion antes de ver el contenido

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .forms import FormularioAbogados, MunicipioForm
import datetime

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

class RegistroView(LoginRequiredMixin, generic.ListView):
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
    #==================================================================
    # login_url = '/login/'
    # redirect_field_name = 'home'
    #==================================================================
    model= DbAbogados
    context_object_name = 'abogados'
    #queryset = DbAbogados.objects.all()[:20]
    queryset = DbAbogados.objects.all()
    template_name = 'registro_abogados/abogados_list.html'
    paginate_by = 10

class AbogadoDetailView(LoginRequiredMixin, generic.DetailView):
    model = DbAbogados
    template_name = 'registro_abogados/abogado_detail.html'
    context_object_name = 'abogado'

#=======================================================================================
# Vista para test Form en Django
#=======================================================================================
#==> SUJETO A VERIFICACION NO FUNCIONO PRUEBA SOLICITUD A FORMULARIO

def get_name(request):
    # si esto es una solicitud POST se necesita procesar la forma de datos
    if request.method == 'POST':
        # se crea una instancia forma y poblamos esta con datos de la solicitud
        form = FormularioAbogados(request.POST)
        # verifica si es valido
        if form.is_valid():
            # procesa los datos en form.cleaned_data como requerido
            # ...
            # redirige a una nueva URL:
            return HttpResponseRedirect('/Gracias/')
    
    # si un GET (u otros muchos metodos) pueden ser creadeos en blanco
    else:
        form = FormularioAbogados()
    
    return render(request, 'formularios.html', {'form':form})

def regAbogado(request):

    if request.method == 'POST':
        form = FormularioAbogados(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            print(name, email)
    else:
        form = FormularioAbogados()
        
    return render(request, 'registro_abogados/form.html', {'form':form})

def municipioDetail(request):

    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():         
            print("valid")
            form.save()

    form = MunicipioForm()
    return render(request, 'registro_abogados/form.html', {'form':form})

#========================================================================================
# EDITANDO VISTAS GENERICAS
#========================================================================================
class AbogadoCreate(LoginRequiredMixin, CreateView):
    model = DbAbogados
    fields = '__all__'
    template_name = 'registro_abogados/abogado_form.html'
    context_object_name = 'abogado'

class AbogadoUpdate(UpdateView):
    model = DbAbogados
    fields = '__all__'

class AbogadoDelete(LoginRequiredMixin, DeleteView):
    model = DbAbogados
    #success_url = reverse_lazy('authors')
    template_name = 'registro_abogados/abogado_confirm_delete.html'
    context_object_name = 'abogado'


   



