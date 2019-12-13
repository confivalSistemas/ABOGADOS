from django.contrib import admin
from .models import DbAbogados, Genero, Municipio, Perfil
# # Register your models here.

#admin.site.register(DbAbogados)
#===========================================================================================================
#=> PERSONALIZANDO DBABOGADOS
class DbAbogadosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombres', 'apellidos', 'cedula', 'tarjeta_p', 'actualizacion', 'ciudad', 'genero', 'perfil',)
    list_filter = ('nombres', 'cedula')
    search_fields = [
        'codigo',
        'nombres',
        'apellidos', 
        'cedula',
        'tarjeta_p',
        'fecha_nacimiento',
        'direccion',
        'ciudad__codigo',
        'ciudadnombre',
        'departamento', 
        'direccion2',
        'ciudad2__codigo',
        'perfil__perfil',
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
        'actualizacion__nombre',
        'observaciones',
        'copiacc',
        'copiatp',
        'fechaexpedicion',
        'ciudadexpedicion__codigo',
        'genero__genero',     
    ]  
    #search_fields = ['genero__genero',]
    fieldsets = (
        ('Datos', {
            'fields': ('nombres', 'apellidos', 'fecha_nacimiento', 'genero', 'cedula', 'fechaexpedicion', 'ciudadexpedicion', 'tarjeta_p', 'perfil')
        }),

        ('Contacto', {
            'fields': ('celular', 'celular1', 'celular2', 'fijo', 'fijo1', 'fijo2', 'fax', 'e_mail1', 'e_mail2')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad', 'direccion2', 'ciudad2')
        }),

        ('Información Adicional', {
            'fields': ('empresa', 'fecha_actualizacion', 'actualizacion', 'observaciones', 'contacto')
        }),        
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



