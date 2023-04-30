from django.urls import path
from .views import *
from . import views

app_name = 'sprint'

urlpatterns = [
    path('', views.lista_sprints, name='listasprints'),
    path('crearsprint', views.crear_sprint, name='crearsprint'),
    path('actualizarsprint/<int:pk>', views.actualizar_sprint, name='actualizarsprint'),
    path('eliminarsprint/<int:pk>', views.eliminar_sprint, name='eliminarsprint'),
]