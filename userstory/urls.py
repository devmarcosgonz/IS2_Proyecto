from django.urls import path
from .views import *
from . import views

app_name = 'userstory'

urlpatterns = [
    path('', views.lista_userstories, name='listauserstories'),
    path('crearuserstory', views.crear_userstory, name='crearuserstory'),
    path('actualizaruserstory/<int:pk>', views.actualizar_userstory, name='actualizaruserstory'),
    path('eliminaruserstory/<int:pk>', views.eliminar_userstory, name='eliminaruserstory'),
]