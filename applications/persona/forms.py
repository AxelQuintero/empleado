from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        """Meta definition fos Empleadoform."""

        model = Empleado
        fields = ('first_name',
                  'last_name',
                  'job',
                  'departamento',
                  'avatar',
                  'habilidades'
                  )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }