from django.contrib import admin
from .models import Seguimiento, TipoSeguimiento, Subitemseguimiento, AsesoresDb, DbAbogados
# Register your models here.

#admin.site.register(Seguimiento)
#===========================================================================================================
#=> PERSONALIZANDO SEGUIMIENTO
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_apellido', 'actividad', 'fecha', 'reprogramar', 'nombre', 'observacion', 'estado')
admin.site.register(Seguimiento, SeguimientoAdmin)