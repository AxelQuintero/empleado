from django.shortcuts import render
# Importar vistas genéricas
from django.views.generic import TemplateView, ListView, CreateView
# Import Models
from .models import Prueba
from .forms import PruebaForm
# Create your views here.

# Cada Vista Genérica tiene sus propios parámetros.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html' # Cuando se habla de un template es básicamente un html

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['1','10','20','30']


class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba # A que tabla se hará referencia para listar
    context_object_name = 'lista'
    # La lista que nos trae es del modelo prueba registrado en el administador (Mediante el Navegador).
    # Es decir, hace una consulta a la base de datos y trae lo que encontró.
    # Traerá lo específicado en la función que se fijó como __str__ (en este caso título + "-" + subtitulo)

class PruebaCreatView(CreateView):
    # Para crear Registros sin meterse uno al Administrador.
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    # fields = ['titulo', 'subtitulo', 'cantidad'] Antes era así
    success_url = '/' # Ir a la página de inicio.