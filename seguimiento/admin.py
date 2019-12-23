# from django.contrib import admin
# from .models import Seguimiento, TipoSeguimiento, Subitemseguimiento, AsesoresDb, DbAbogados
# # Register your models here.

# #admin.site.register(Seguimiento)
# #===========================================================================================================
# #=> PERSONALIZANDO SEGUIMIENTO
# class SeguimientoAdmin(admin.ModelAdmin):
#     list_display = ('nombre_apellido', 'actividad', 'fecha', 'reprogramar', 'nombre', 'observacion', 'estado')
#     search_fields = [
#         'codigo',
#         'nombre_apellido__nombres', # => solo consulta por nombre del abogado, revisar el llamado por concatenacion
#         'actividad',
#         'fecha',
#         'reprogramar',
#         'nombre__nombre', # => solo consulta por nombre del asesor, revisar el llamado por concatenacion
#         'observacion',
#         'estado__subsegumiento',
#     ]

#     # fieldsets = (
#     #     ('Datos', {
#     #         'fields': ('',)
#     #     }),
#     # )

# admin.site.register(Seguimiento, SeguimientoAdmin)