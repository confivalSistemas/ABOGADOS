from django.contrib import admin
from .models import AsesoresDb, Genero, Municipio, Perfilasesor, Comisiones
# Register your models here.

#admin.site.register(AsesoresDb)
#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB

class AsesoresDbAdmin(admin.ModelAdmin):
    list_display = ('cod_asesor', 'nombre', 'apellido', 'comision', 'genero')
    list_filter = ('cod_asesor', 'nombre')
    search_fields = [
        'cod_asesor',
        'nombre',
        'apellido',
        'direccion',
        'ciudad__municipio',
        'direccion2',
        'ciudad2__municipio',
        'celular',
        'mail',
        't_asesor',
        'comision__tipo',
        'cedula',
        'c_cedula',
        'fecha',
        'fecha_s',
        'perfil',
        'fechanacimiento',
        'fechaexpedicion',
        'ciudadexpedicion__municipio',
        'genero__genero',
    ]
    
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('nombre', 'apellido', 'cedula', 'fechanacimiento', 'fechaexpedicion', 'ciudadexpedicion', 'genero', 'perfil')
        }),

        ('Contacto', {
            'fields': ('celular', 'mail', 't_asesor')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad', 'direccion2', 'ciudad2')
        }),

        ('Información Adicional', {
            'fields': ('comision', 'c_cedula', 'fecha', 'fecha_s')
        }),
    )

admin.site.register(AsesoresDb, AsesoresDbAdmin)
    
#admin.site.register(Perfilasesor)
#===========================================================================================================
#=> PERSONALIZANDO PERFILASESOR
@admin.register(Perfilasesor)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'perfil')
    list_filter = ('codigo','perfil')

#admin.site.register(Comisiones)
#===========================================================================================================
#=> PERSONALIZANDO COMISIONES
@admin.register(Comisiones)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion', 'valor')
    
