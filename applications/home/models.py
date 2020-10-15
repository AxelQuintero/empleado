from django.db import models

# Create your models here.

# Interacción de Bases de Datos.

# Para conocer los cambios en los modelos es: python manage.py makemigrations
# Para realizar los cambios en la base de datos es: python manage.py migrate
# Una vez que se migra aparecera en migrations de cada applicación
# Correr de nuevo: python manage.py runserver
class Prueba(models.Model):
    # Esto se convertirá en automático en código sql mediante la ORM(Transforma el código)
    titulo = models.CharField(max_length = 100)
    subtitulo = models.CharField(max_length = 50)
    cantidad = models.IntegerField()
    

    def __str__(self):
        return self.titulo + "-" + self.subtitulo
