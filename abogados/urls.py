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
    #===============================================================
    #=> lo anterior añade automaticamente las siguientes 
    # path("accounts/login/ [name='login']", include('django.contrib.auth.urls')),
    # path("accounts/logout/ [name='logout']", include('django.contrib.auth.urls')),
    # path("accounts/password_changue/ [name='password_change']", include('django.contrib.auth.urls')),
    # path("accounts/password_changue/done/ [name='password_change_done']", include('django.contrib.auth.urls')),
    # path("accounts/password_reset/ [name='password_reset']", include('django.contrib.auth.urls')),
    # path("accounts/password_reset/done/ [name='password_reset_done']", include('django.contrib.auth.urls')),
    # path("accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/ [name='password_reset_confirm']", include('django.contrib.auth.urls')),
    # path("accounts/reset/done/ [name='password_reset_complete']", include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

