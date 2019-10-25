# Configuración Proyecto Django-Python para registro de abogados en CONFIVAL

Es un aplicativo en desarrollo para migración de aplicativos de areas comercial, juridica entre otras que estan
implementadas en la actualidad en php y bases de datos Mysql. El objetivo es cambiar lenguaje de programación a Python 
para mayor escalabilidad y analisis de datos con los procesos de la empresa. 

## Instalación
A continuacion se presentan los requerimientos para configuracion de ambiente de trabajo 


1. Desinstalar versiones de python desactualizadas
2. Instalar [python](https://www.python.org/downloads/windows/) 64 ultima version 3.7
```bash
Download Windows x86-64 executable installer
```
3. instalar django CMD o linea de comandos en Windows
```bash
pip install Django==2.2.6
python -m django --version
```
4. instalar https://visualstudio.microsoft.com/es/downloads/?rr=https%3A%2F%2Fwww.google.com%2F ARM64 o 64x segun procesador.
Esto con el objetivo de solucionar error de dependencias 
```bash
cd error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.
```
5. Crear proyecto python startproject "nombre_del_proyecto"
```bash
django-admin startproject abogados
```
cambiar nombre del directorio raiz

```bash
ABOGADOS/
    manage.py
    abogados/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
correr el servidor de desarrollo
```bash
python manage.py runserver

ctrl + c  
```
6. Instalar libreria de conexión a base de datos en Mysql en terminal 
```bash
pip install mysqlclient
```
7. Crear applicativo registro_abogados dentro del directorio raiz del proyecto ABOGADOS
```bash
python manage.py startapp registro_abogados
```
```bash
registro_abogados/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
8. Configurar abogados/setting.py para conexion a base de datos existente Mysql en variable DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',#asignar ruta de archivo conexion.cnf
        },
    }
}
```

9. crear archivo 'conexion.cnf' en directorio del aplicativo  registro_abogados => registro_abogados/conexion.cnf

```bash
[client]
database = NAME #(nombre de la base de datos)
user = USER #(usuario)
password = PASSWORD #(contraseña)
default-character-set = utf8
```


## Para la configuración de bases de datos existente y conexión a Django importando contenido de tablas 

10. Eliminar sistema de seguridad que esta contenido en script.msql como son
```bash
.auth
.django
.sc_
```
	
11. Se guarda el archivo de la base de datos limpia con un nombre "confival.msql" para ser utilizada en 
app registro_abogados django

12. Aplicar comando de migración para detectar base de datos y creacion de tablas de seguridad
```bash
python manage.py migrate
```

13. Traer las tablas en db confival al modelo de nuestra aplicacion models.py de registro_abogados
con el siguiente comando

```bash
python manage.py inspectdb > registro_abogados/models.py
```

14. activar modelos en setting.py incluir la app: registro_abogados con el nombre de la clase creada en apps.py
```python
INSTALLED_APPS = [
    'registro_abogados.apps.RegistroAbogadosConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

15. Ajustar tipo de archivo generado para models.py por inspectdb utf16 -> utf8

16. Aplicar comando de migración
```bash
python manage.py migrate
```
17. Aplicar comando de migracion a la app
```bash
python manage.py makemigrations registro_abogados
```

18. Aplicar comando de migración al archivo del directorio migrations para que Django reconsca todos los modelos 
como tablas y campos respectivos para su utilización

```bash
python manage.py sqlmigrate registro_abogados 000x  # x es el numero de la migración creada
```	

## Para la creación de vista administrador en Django

19. Ejecutar usuario de app con comando python 
```bash
manage.py createsuperuser
```
```bash
Username: confival
Email:prueba@prueba.com
Password:12345
```

20. Ejecutar servidor para ingresar a la vista de administrador http://localhost:8000/admin/
```bash
python manage.py runserver
```

21. Configurar archivo admin.py de app registro_abogados para reconocimiento de modelos desde administrador

## Usage

```python

from django.contrib import admin
from .models import DbAbogados

admin.site.register(DbAbogados)
```
