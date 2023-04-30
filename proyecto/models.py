from django.db import models

# Create your models here.

class Proyectos(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)

    class Meta:
        db_table = 'proyectos'
        verbose_name_plural = 'proyectos'
        verbose_name = 'proyecto'

    def __str__(self):
        return self.nombre_proyecto