from django import forms
from .models import EstadosUserStory

class EstadosUserStoryForm(forms.ModelForm):
    class Meta:
        model = EstadosUserStory
        fields = ['id_estado', 'descripcion_estado']