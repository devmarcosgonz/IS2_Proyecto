from django.urls import path
from .views import *
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.lista_usuarios, name='listausuarios'),
    path('crearusuario', views.crear_usuario, name='crearusuario'),
    path('actualizarusuario/<int:pk>', views.actualizar_usuario, name='actualizarusuario'),
    path('eliminarusuario/<int:pk>', views.eliminar_usuario, name='eliminarusuario'),
]