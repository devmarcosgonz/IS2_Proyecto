from django.urls import path
from .views import *
from . import views

app_name = 'rol'

urlpatterns = [
    path('', views.lista_roles, name='listaroles'),
    path('crearrol', views.crear_rol, name='crearrol'),
    path('actualizarrol/<int:pk>', views.actualizar_rol, name='actualizarrol'),
    path('eliminarrol/<int:pk>', views.eliminar_rol, name='eliminarrol'),
]