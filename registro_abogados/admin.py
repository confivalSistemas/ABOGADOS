from django.contrib import admin
from .models import DbAbogados, Genero, Municipio, Perfil
# # Register your models here.

#admin.site.register(DbAbogados)
#===========================================================================================================
#=> PERSONALIZANDO DBABOGADOS
class DbAbogadosAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'tarjeta_p', 'fecha_nacimiento', 'direccion', 'ciudad', 'ciudadnombre')
    list_filter = ('nombres', 'cedula')
    search_fields = (
        'codigo',
        'nombres',
        'apellidos', 
        'cedula',
        'tarjeta_p',
        'fecha_nacimiento',
        'direccion',
        'ciudadnombre',
        'departamento', 
        'direccion2',
        'empresa',
        'celular2',
        'celular1',
        'celular',
        'fijo2',
        'fijo1',
        'fijo',
        'fax',
        'e_mail1',
        'e_mail2',
        'contacto',
        'fecha_actualizacion',
        'observaciones',
        'copiacc',
        'copiatp',
        'fechaexpedicion',     
    )   
                        
                        



admin.site.register(DbAbogados, DbAbogadosAdmin)

#admin.site.register(Municipio)
#===========================================================================================================
#=> PERSONALIZANDO MUNICIPIO
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'codigo_dane', 'departamento', 'municipio')
    list_filter = ('codigo', 'departamento')

#admin.site.register(Perfil)
#===========================================================================================================
#=> PERSONALIZANDO PERFIL
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'perfil')
    list_filter = ('codigo','perfil')

#admin.site.register(Genero)
#===========================================================================================================
#=> PERSONALIZANDO GENERO
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero', 'abreviatura', 'codigo')
    list_filter = ('codigo','abreviatura')


