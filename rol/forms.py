from django import forms
from .models import Roles

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['id_rol', 'descripcion_rol']