from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):

    habilidad = models.CharField("Habilidad", max_length = 50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return str(self.id) + "-" + self.habilidad

# Create your models here.
class Empleado(models.Model): 
    """ Modelo para tabla Empleado. """

    Job_Choices = (
        ('0',"CONTADOR"),
        ('1',"ADMINISTRADOR"),
        ('2', "ECONOMISTA"),
        ('3', "OTRO")
    )
    # Trabajos como: Contador, Economista, Otro.
    first_name = models.CharField("Nombres", max_length = 60)
    last_name = models.CharField("Apellidos", max_length = 60)
    full_name = models.CharField('Nombres Completos', max_length = 120, blank = True)
    job = models.CharField("Trabajo", max_length = 1, choices = Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'empleado', blank = True, height_field = None, width_field = None) # La imagen se subirá en la carpeta media configurada y se creará la carpeta empleado
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    # Cuando se realiza el migrate por RichTextField ya existen registros sin este atributo,
    # por lo tanto, en las opciones que aparecen seleccionamos la uno y posteriormente ingresamos "Texto".
    

    class Meta:
        verbose_name = 'Mis Empleados'
        verbose_name_plural = 'Mi Equipo de Trabajo'
        ordering = ['id']
        # Para que no se repitan
        unique_together = ('first_name','last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name