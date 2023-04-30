from django import forms
from .models import UserStory

class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ['id_userstory', 'nombre', 'descripcion', 'story_point', 'definicion_hecho', 'prioridad', 'id_estado', 'fecha_inicio', 'fecha_fin', 'id_sprint', 'id_proyectousuario']