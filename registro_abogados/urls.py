from django.urls import path

from . import views

app_name = 'registro_abogados'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('registro/', views.RegistroView.as_view(), name= 'registro'),
    path('formulario/', views.FormularioView.as_view(), name = 'formulario'),
]