"""abogados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# para carga de archivos
from django.conf import settings
from django.conf.urls.static import static

# para tomar URL relativas a ridereccionar
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# para personalizacion de administrador
admin.site.site_header = 'Administración de aplicativos Confival'
admin.site.site_title = 'Administración Confival'
admin.site.index_title = 'Sitio administración CRM'

urlpatterns = [
    path('home/', include('registro_abogados.urls')),    
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    
    # Add Django site authentication urls (for login, logout, password management )
    path('accounts/', include('django.contrib.auth.urls')),   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

