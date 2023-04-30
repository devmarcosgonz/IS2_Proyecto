from django.urls import path
from .views import *
from . import views

app_name = 'proyectousuario'

urlpatterns = [
    path('', views.lista_proyectousuarios, name='listaproyectousuarios'),
    path('crearproyectousuario', views.crear_proyectousuario, name='crearproyectousuario'),
    path('actualizarproyectousuario/<int:pk>', views.actualizar_proyectousuario, name='actualizarproyectousuario'),
    path('eliminarproyectousuario/<int:pk>', views.eliminar_proyectousuario, name='eliminarproyectousuario'),
]