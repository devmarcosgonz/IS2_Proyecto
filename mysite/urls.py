"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('usuarios/', include('usuario.urls')),
    #falta implementar el estado activo e inactivo al momento de "eliminación de un usuario" para no perder el historial del usuario
    # path('estadouser/', include('estadouser.urls')),
    path('proyectos/', include('proyecto.urls')),
    path('roles/', include('rol.urls')),
    path('asignar/', include('proyectousuario.urls')),
    path('sprint/', include('sprint.urls')),
    path('estadouserstory/', include('estadouserstory.urls')),
    path('userstory/', include('userstory.urls')),
]
