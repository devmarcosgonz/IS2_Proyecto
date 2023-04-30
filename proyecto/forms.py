from django import forms
from .models import Proyectos

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['id_proyecto', 'nombre_proyecto']