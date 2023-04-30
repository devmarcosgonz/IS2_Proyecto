from django.db import models

# Create your models here.

class EstadosUserStory(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion_estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'estados_userstory'
        verbose_name_plural = 'estadosuserstories'
        verbose_name = 'estadouserstory'

    def __str__(self):
        return self.descripcion_estado