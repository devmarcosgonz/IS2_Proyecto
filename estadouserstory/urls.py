from django.urls import path
from .views import *
from . import views

app_name = 'estadouserstory'

urlpatterns = [
    path('', views.lista_estadouserstories, name='listaestadouserstories'),
    path('crearestadouserstory', views.crear_estadouserstory, name='crearestadouserstory'),
    path('actualizarestadouserstory/<int:pk>', views.actualizar_estadouserstory, name='actualizarestadouserstory'),
    path('eliminarestadouserstory/<int:pk>', views.eliminar_estadouserstory, name='eliminarestadouserstory'),
]