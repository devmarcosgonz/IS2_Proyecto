from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id_usuario', 'nombre_usuario', 'usuario_sistema', 'contrasenha', 'is_active']