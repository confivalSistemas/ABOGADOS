from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#aca se tienen que llamar a los modelos
from .models import DbAbogados

# Create your views here.
def index(request):
    return HttpResponse("BIENVENIDO AL REGISTRO DE ABOGADOS DE CONFIVAL")

def registro(request):
    latest_abogado_list = DbAbogados.objects.order_by('codigo')
    template = loader.get_template('registro_abogados/prueba_register.html')
    context = {
        'latest_abogado_list': latest_abogado_list,
    }
    return HttpResponse(template.render(context, request))  