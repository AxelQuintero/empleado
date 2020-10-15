from django.contrib import admin
from django.urls import path
from . import views  # Importamos todo el archivo
urlpatterns = [
    path("prueba/",views.PruebaView.as_view()), # Con el .as_view() se ejecuta una vista genérica (vista con clases).
    path("lista/", views.PruebaListView.as_view()),
    path("lista-prueba/", views.ListarPrueba.as_view()),
    path("add/", views.PruebaCreatView.as_view(), name = 'prueba_add'),
    path("resumen-foundation/", views.ResumenFoundationView.as_view(), name = 'resumenF')
]
