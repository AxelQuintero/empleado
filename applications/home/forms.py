from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba 
        fields = ('titulo',
                  'subtitulo',
                  'cantidad',)
    
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese texto aquí'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese texto aquí'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'placeholder':'Ingrese texto aquí'
                }
            )
        }
        
    def clean_cantidad(self):
        # Recuparamos lo que se ha enviado
        cantidad = self.cleaned_data['cantidad']
        if cantidad<10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        # Si si lo cumple solo regresa la cantidad
        return cantidad