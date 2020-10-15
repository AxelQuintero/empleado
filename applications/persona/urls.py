from django.contrib import admin
from django.urls import path
from . import views  # Importamos todo el archivo

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name = 'inicio'),
    path('listar-todo-empleados/', views.LisAllEmpleados.as_view(), name = "empleados_all"),
    path('listar-by-area/<shortname>/', views.ListByAreaEmpleado.as_view(), name = "listbyarea"),
    path('listar-empleados-admin/', views.ListEmpleadosAdmin.as_view(), name = "empleados_admin"),
    path('listar-by-job/<job>/', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades-empleado/<id>/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name = "Empleado_Detail"), # También crea interamente un pk (como el id).
    path('adds-empleado/', views.EmpleadoCreatView.as_view(), name = "empleado_add"),
    path('success/', views.SuccessView.as_view(), name = 'correcto'), # Name es para reverse_lazy
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name = 'modificar_empleado'),
    path('delete/<pk>/', views.EmpleadoDelateView.as_view(), name = 'eliminar_empleado'),
]


