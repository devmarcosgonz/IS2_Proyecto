from django.db import models
from usuario.models import Usuarios
from proyecto.models import Proyectos
from rol.models import Roles

# Create your models here.

class ProyectoUsuario(models.Model):
    id_proyecto_usuario = models.IntegerField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuario_proyecto'
        verbose_name_plural = 'proyectousuarios'
        verbose_name = 'proyectousuario'

    def __str__(self):
        texto = self.id_usuario.nombre_usuario + " (" + self.id_rol.descripcion_rol + ")"
        return texto