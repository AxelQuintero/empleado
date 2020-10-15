from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    # El display que se hace con toda la información
    list_display = (
        "id",
        "first_name",
        "last_name",
        "departamento",
        "job",
        "fullname",
        "avatar",
    )

    # fullname no existe en la classe Emppleado de Models
    def fullname(self, obj):
        # Cualquier operación que necesite. Obj es lo que regresa Empleado en __str__. Si se pinta en 
        # consola con print, itera sobre cada valor guardado ya en el admi de Django.
        return obj.first_name + " " + obj.last_name


    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    # Este solo funciona para relaciones muchos a muchos
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)