from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path("new-departamento/", views.NewDepartamentoView.as_view(), name = "new_departamento"), # Ejecuta lo que sigue después de la coma.
    path("departamento_list/", views.DepartamentoListView.as_view(), name = "new_depa"),
]
