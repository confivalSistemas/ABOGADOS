from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'registro_abogados'

urlpatterns = [
    path('', views.index, name='index'),
    # rutas para abogados
    path('abogadosRegistrados/', views.AbogadosRegistradosView.as_view(), name = 'abogadosRegistrados'),
    path('abogadosRegistrados/<int:pk>', views.AbogadoDetailView.as_view(), name = 'abogado-detail'),
    path('registro/', views.RegistroView.as_view(), name= 'registro'),
    path('formulario/', views.FormularioView.as_view(), name = 'formulario'),

    # rutas para crear, actualizar y borrar abogados
    path('abogado/create/', views.AbogadoCreate.as_view(), name='abogado_create'),
    path('abogado/<int:pk>/update', views.AbogadoUpdate.as_view(), name='abogado_update'),
    path('abogado/<int:pk>/delete', views.AbogadoDelete.as_view(), name='abogado_delete'),

    # rutas para formas
    path('createAbogado', views.regAbogado),
    path('createMunicipio', views.municipioDetail),
]
