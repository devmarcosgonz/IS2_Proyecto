from django import forms
from .models import Sprints

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprints
        fields = ['id_sprint', 'nombre_sprint', 'fecha_inicio', 'fecha_fin_prev', 'fecha_fin']