from django.db import models

# Create your models here.
# 
class Departamento(models.Model):
    # Para conocer todos los fields: https://docs.djangoproject.com/en/3.1/ref/models/fields/
    # Campos Obligatorios
    name = models.CharField('Nombre', max_length = 50, null = True) 
    # Si ponemos , blank = True podrá no ser obligatorio
    # Si ponemos, null = True requiere un valor obligatoriamente. 
    # Si ponemos, editable = False No nos dejará acceder porque seguramente el campo se generará internamente.
    short_name = models.CharField('Nombre Corto', max_length = 20, unique = True)
    # Unique = True es que ningún otro campo será igual.
    # No obligatorio
    anulate = models.BooleanField('Anulado', default = False)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['id']
        unique_together = ('name','short_name') # La combinación de name y shortname no se puede repetir
        
    # Internamente genera un id para cada una de las tablas.
    def __str__(self):
        return  str(self.id) + " - " + self.name + " - " + self.short_name 