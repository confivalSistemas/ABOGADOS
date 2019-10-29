from django.urls import path

from . import views

app_name = 'registro_abogados'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name= 'registro'),
]