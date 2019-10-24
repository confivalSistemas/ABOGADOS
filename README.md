cd error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.

////////////////
=======================================================================================================================================
CONFIGURACION PROYECTO DJANGO EN WINDOWS
=======================================================================================================================================

1. desinstalar python
2. instalar python 64 ultima version 3.7
3. instalar django CMD pip install Django
4. intalar https://visualstudio.microsoft.com/es/downloads/?rr=https%3A%2F%2Fwww.google.com%2F ARM64 o 64x segun procesador
5. crear proyecto python startproject "nombre"
6. instalar pip install mysqlclient en consola
7. crear app django-admin manage.py startapp "nombre app"
8. configurar setting.py
    "# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
"
9. crear archivo en el carpeta del app tipo .cnf segun modelo conexion:

conexion.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
=========================================================================================================================================
PARA LA CONFIGURACION DE BASE DE DATOS Y CONEXION A DJANGO IMPORTANDO CONTENIDO DE TABLAS 
=========================================================================================================================================

10. Eliminar sistema de seguridad que esta contenido en script.msql como son
	*.auth
	*.django
	*.sc_
11. Se guarda el archivo de la base de datos limpia con un nombre "confival.msql" para ser utilizada en 
app registro_abogados django

12. Aplicar comando de migración
	python manage.py migrate

13. Traer las tablas en db confival al modelo de nuestra aplicacion models.py de registro_abogados
con el siguiente comando
	python manage.py inspectdb > registro_abogados/models.py

14. activar modelos 
   a- setting.py incluir la app:
	segun modelo:
	'db_abogados.DbAbogadosConfig'

15. Ajustar tipo de archivo generado para models.py por inspectdb utf16 -> utf8

16. Aplicar comando de migración
	python manage.py migrate

17. Aplicar comando de migracion a la app
	python manage.py makemigrations registro_abogados

18. Aplicar comando de migracion al archivo del directorio migrate
	python manage.py sqlmigrate registro_abogados 000x  => x es el numero de la migración creada
	

===========================================================================================================================================
PARA LA CREACION DE VISTAS DE ADMINISTRADOR EN DJANGOpython
===========================================================================================================================================

18. Ejecutar usuario de app con comando python manage.py createsuperuser
	*Username: confival
	*Email:prueba@prueba.com
	*Password:12345

19. Ejecutar servidor para ingresar a la vista de administrador
	*python manage.py runserver

20. Configurar archivo admin.py de app registro:usuario para reconocimiento de modelos desde administrador+

	from django.contrib import admin

	from .models import DbAbogados

	admin.site.register(DbAbogados)