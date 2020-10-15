from django import forms

class NewDepartamentoForm(forms.Form): # Como será un nuevo departameno no utilizamos forms.ModelForm como en home.
    nombre = forms.CharField(max_length = 50, 
                            widget = forms.TextInput(attrs = {"placeholder":"Nombre(s)"}))
    apellido = forms.CharField(max_length = 50,
                            widget = forms.TextInput(attrs = {"placeholder":"Apellido(s)"}))
    departamento = forms.CharField(max_length = 100,
                            widget = forms.TextInput(attrs = {"placeholder":"Departamento"}))
    short_name_departamento = forms.CharField(max_length = 20,
                            widget = forms.TextInput(attrs = {"placeholder":"Breviatura"}))

