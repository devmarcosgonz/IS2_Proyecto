from django.db import models
from datetime import date, timedelta

# Create your models here.

class Sprints(models.Model):
    id_sprint = models.IntegerField(primary_key=True)
    nombre_sprint = models.CharField(max_length=10)
    fecha_inicio = models.DateField(default = date.today().strftime("%Y-%m-%d"))
    fecha_fin_prev = models.DateField(default = (date.today() + timedelta(days=14)).strftime("%Y-%m-%d"))
    fecha_fin = models.DateField(null=True)

    class Meta:
        db_table = 'sprints'
        verbose_name_plural = 'sprints'
        verbose_name = 'sprint'

    def __str__(self):
        return self.nombre_sprint