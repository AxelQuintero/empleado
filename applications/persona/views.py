from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
# Models
from .models import Empleado
# Forms
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    """Vista que carga la página de inicio."""
    template_name = "inicio.html"


class ListEmpleadosAdmin(ListView):
    # Atributos que se pueden poner en la función: https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10 #http://127.0.0.1:8000/listar-todo-empleados/?page=1 si le cambiamos a dos, 
    # seguirán los siguientes 4.
    ordering = "first_name"
    context_object_name = "empleados"
    model = Empleado # De donde obtendrá los atributos. con el queryset lo quitamos
    # Si no está el queryset se necesita teer el model


# 1.- Listar todos los empleados de la empresa.
class LisAllEmpleados(ListView):
    # Atributos que se pueden poner en la función: https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
    template_name = 'persona/list_all.html'
    paginate_by = 4 #http://127.0.0.1:8000/listar-todo-empleados/?page=1 si le cambiamos a dos, 
    # seguirán los siguientes 4.
    ordering = "first_name"
    context_object_name = "empleados"
    # model = Empleado # De donde obtendrá los atributos. con el queryset lo quitamos

    # context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'') # Interceptar solicitudes que se han hecho con el get
        # las "", se ponen para que sea una tupla.
        lista = Empleado.objects.filter(full_name__icontains = palabra_clave)
        # Filtra el fullname por la palabra clave. Busca la cadena en la lista de fullnames.
        return lista


# 2.- Listas todos los empleaos que pertenecen a un área de la empresa
class ListByAreaEmpleado(ListView):
    """ Lista Empleados por Área. """
    template_name = "persona/list_by_area.html"
    context_object_name = "empleados"
    # Aplicar filtros
    # queryset = Empleado.objects.filter(departamento__short_name = 'contabilidad') # Acceder al atributo
    # de la clase Departamento que se mando a traer mediante en la clase modelos de ahí mismo.

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        # Recogeremos en la url elemento en <shortname>
        area = self.kwargs["shortname"]
        lista = Empleado.objects.filter(departamento__short_name = area)
    
        return lista


 # 3.- Listar empleados por trabajo.   
class ListByJobEmpleado(ListView):
    """ Listar Empleados por Trabajo. """
    
    template_name = "persona/list_by_job.html"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # Recogeremos en la url elemento en <job
        area = self.kwargs["job"]
        Job_Choices = (
        ('0',"CONTADOR"),
        ('1',"ADMINISTRADOR"),
        ('2', "ECONOMISTA"),
        ('3', "OTRO")
        )
        Job_Choices = {l:d for d,l in Job_Choices}
        lista = Empleado.objects.filter(job  = Job_Choices.get(area))
    
        return lista


 # 4.- Listar los empleados por palabra clave.
class ListEmpleadosByKword(ListView):
    """ Lista Empleado por palabra clabe. """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'') # Intercepatr solicitudes que se han hecho con el get
        # las "", se ponen para que sea una tupla.
        lista = Empleado.objects.filter(first_name = palabra_clave)
        return lista


# 5.- Listar habilidades de un empleado.
class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        # ManytoMany Django: https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
        palabra_clave = self.kwargs["id"]
        # Ya no será filter porque solo deseo recuperar un único registro.
        empleado = Empleado.objects.get(id = palabra_clave)
        return empleado.habilidades.all() 


# DetailView
class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado # Recupera la información pasada en la url de <pk>

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs) # Lo envía como contexto al template
        context["titulo"] = "Empleado del Mes"
        return context


# Para redireccionar a una página en la clase de EmpleadoCreateView (La de Abajo).
class SuccessView(TemplateView):
    template_name = "persona/success.html"


# CreateView
class EmpleadoCreatView(CreateView):
    template_name = "persona/adds.html"
    model = Empleado
    # Parámetro extra para Create View (Debe de hacer referencia a algún campo del modelo Empleado)
    # Los campos que va a recoger cuando cree en la base de datos.
    #fields = ['first_name','last_name','job']
    # fields = ("__all__") # Para jalar todos los campos
    #fields = ["first_name", los quitamos porque pusimos la form_class
    #          "last_name",
    #          "departamento",
    #          "job",
    #          "habilidades",
    #          "avatar",]
    form_class = EmpleadoForm
    # URL a la que debe de redireccionarse cuando acabe el llenado de información.
    # success_url = '.' # Redirecciona a la misma página.
    #success_url = '/success' # Redirecciona a otra página.

    # Con reverse_lazy
    success_url = reverse_lazy('persona_app:empleados_admin') # persona app es el nombre que se les dio a todas 
    # las urls y correcto la que se dió a la url de success.

    # Comentamos en admin la función de fullname para hacerlo de esta manera. Se guardará solo 
    # con los nuevos que ingresan.
    def form_valid(self, form):
        empleado = form.save() # Almacena el formulario en esta variable.
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreatView,self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ["first_name",
              "last_name",
              "departamento",
              "job",
              "habilidades"]

    success_url = reverse_lazy('persona_app:empleados_admin')

    # Primero se ejecuta esta antes del form_valid sin importar cual se declare primero. Ya que
    # Se jalan los datos por cualquier cosa.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("********Post**********")
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print("********Form Valid**********")
        print(form)
        return super(EmpleadoUpdateView,self).form_valid(form)


class EmpleadoDelateView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:empleados_admin")
    # La acción se realiza con el formulario en el html