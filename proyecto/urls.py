from django.urls import path
from .views import *
from . import views

app_name = 'proyecto'

urlpatterns = [
    path('', views.lista_proyectos, name='listaproyectos'),
    path('crearproyecto', views.crear_proyecto, name='crearproyecto'),
    path('actualizarproyecto/<int:pk>', views.actualizar_proyecto, name='actualizarproyecto'),
    path('eliminarproyecto/<int:pk>', views.eliminar_proyecto, name='eliminarproyecto'),
]