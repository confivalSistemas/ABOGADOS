from django.contrib import admin
from .models import AsesoresDb, Genero, Municipio, Perfilasesor, Comisiones
# Register your models here.

#admin.site.register(AsesoresDb)
#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB

class AsesoresDbAdmin(admin.ModelAdmin):
    list_display = ('cod_asesor', 'nombre', 'apellido')
    list_filter = ('cod_asesor', 'nombre')
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
    
