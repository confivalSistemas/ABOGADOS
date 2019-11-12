from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'registro_abogados'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('registro/', views.RegistroView.as_view(), name= 'registro'),
    path('formulario/', views.FormularioView.as_view(), name = 'formulario'),
]