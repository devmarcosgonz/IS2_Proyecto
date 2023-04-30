from django.db import models
from datetime import date
from proyectousuario.models import ProyectoUsuario
from estadouserstory.models import EstadosUserStory
from sprint.models import Sprints

# Create your models here.

class UserStory(models.Model):
    id_userstory = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=8000, null=True, blank=True)
    story_point = models.IntegerField(null=True, blank=True)
    definicion_hecho = models.CharField(max_length=8000, null=True, blank=True)
    prioridad = models.IntegerField(null=True, blank=True, default = 1)

    id_estado = models.ForeignKey(EstadosUserStory, on_delete=models.CASCADE, null=True, blank=True)

    fecha_inicio = models.DateField(null=True, blank=True, default = date.today)
    fecha_fin = models.DateField(null=True, blank=True)
    
    id_sprint = models.ForeignKey(Sprints, on_delete=models.CASCADE, null=True, blank=True)
    id_proyectousuario = models.ForeignKey(ProyectoUsuario, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'user_stories'
        verbose_name_plural = 'userstories'
        verbose_name = 'userstory'

    def __str__(self):
        return self.nombre