from .base import * # Importamos la base de ambos entornos.
# .base es que estará en el mismo nivel.
import os
# Para correr ahora el Manage.py se tiene que especificar cual settings deberá tomar. Por lo tanto, el comando se corre de la siguiente
# Manera: python manage.py runserver --settings=Empleados.settings.local

# Se editó el manage.py y en lugar de tener Empleados.settings (settings hace referencia al .py en este caso)
# El nuevo settings por default está en la carpeta settings/local.py, por lo tanto, lo cambiamos en el manage.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleados',
        'USER': 'if710152',
        'PASSWORD': 'MUQA980214',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/' # acceder a los archivos estáticos.
STATICFILES_DIRS = [os.path.abspath("static")]
# Para archivos multimedia
MEDIA_URL = '/media/'
# Carpeta base o raíz para archivos multimedia
MEDIA_ROOT = os.path.abspath("media")