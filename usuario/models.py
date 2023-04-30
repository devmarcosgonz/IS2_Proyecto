from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    usuario_sistema = models.CharField(max_length=50)
    contrasenha = models.CharField(max_length=20)

    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = 'usuarios'
        verbose_name = 'usuario'
        constraints = [
            models.UniqueConstraint(fields=['usuario_sistema'], name='unique_usuario_sistema')
        ]
        indexes = [
            models.Index(fields=['id_usuario', 'nombre_usuario'], name='idx_usuarios_id_nombre'),
        ]

    def __str__(self):
        return self.nombre_usuario