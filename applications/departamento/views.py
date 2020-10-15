from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView 
from django.views.generic import ListView

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado # Para registrar al empleado
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    # Recuperamos el formulario
    def form_valid(self, form):

        # Crear instancia del Departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name_departamento']
        )
        depa.save() # Para guardarlo en departamento.

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = 1, # ADMINISTRADOR
            departamento = depa
        ) # con el método create se guarda solo. 

        return super(NewDepartamentoView, self).form_valid(form)