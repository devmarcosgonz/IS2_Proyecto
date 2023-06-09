from django.urls import path
from .views import *
from . import views

app_name = 'userstory'

urlpatterns = [
    path('', views.lista_userstories, name='listauserstories'),
    path('crearuserstory', views.crear_userstory, name='crearuserstory'),
    path('actualizaruserstory/<int:pk>', views.actualizar_userstory, name='actualizaruserstory'),
    path('eliminaruserstory/<int:pk>', views.eliminar_userstory, name='eliminaruserstory'),
    path('listasinsprint', views.lista_sinsprint, name='listasinsprint'),
    path('kanbanboard', views.kanban_board, name='kanbanboard'),
    path('burndown/list', views.burndown_list, name='burndownlist'),
    path('burndown/chart/<int:pk>', views.burndown_chart, name='burndownchart'),
]