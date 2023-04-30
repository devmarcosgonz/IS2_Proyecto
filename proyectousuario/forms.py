from django import forms
from .models import Usuarios, Proyectos, Roles, ProyectoUsuario

class ProyectoUsuarioForm(forms.ModelForm):
    class Meta:
        model = ProyectoUsuario
        fields = ['id_proyecto_usuario', 'id_proyecto', 'id_usuario', 'id_rol']