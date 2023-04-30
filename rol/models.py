from django.db import models

# Create your models here.

class Roles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    descripcion_rol = models.CharField(max_length=20)

    class Meta:
        db_table = 'roles'
        verbose_name_plural = 'roles'
        verbose_name = 'rol'

    def __str__(self):
        return self.descripcion_rol