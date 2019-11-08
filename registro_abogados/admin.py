from django.contrib import admin
from .models import DbAbogados, Genero, Municipio, Perfil, AsesoresDb, TipoSeguimiento
# # Register your models here.

#admin.site.register(DbAbogados)
#===========================================================================================================
#=> PERSONALIZANDO DBABOGADOS
class DbAbogadosAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'tarjeta_p', 'fecha_nacimiento', 'direccion', 'ciudad', 'ciudadnombre')
admin.site.register(DbAbogados, DbAbogadosAdmin)

#admin.site.register(Municipio)
#===========================================================================================================
#=> PERSONALIZANDO MUNICIPIO
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Perfil)
#===========================================================================================================
#=> PERSONALIZANDO PERFIL
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Genero)
#===========================================================================================================
#=> PERSONALIZANDO GENERO
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

#admin.site.register(AsesoresDb)
#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB
@admin.register(AsesoresDb)
class AsesoresDbAdmin(admin.ModelAdmin):
    pass
