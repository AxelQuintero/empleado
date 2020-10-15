Proyecto Inicializado como 
django-adming startproject Empleados

Para crear un super usuario en admn:
python manage.py createsuperuser
Nombre de Usuario: (Nombre de Usuario)
Dirección de correo electrónico: (Correo Electrónico)
Password: (Contraseña para el usuario)
Password (again) : (Contraseña para el usuario)


Para Crear la Base de Datos en PostgreSQL:
Server [localhost]: (Enter sin ingresar nada)
Database [postgres]: (Enter sin ingresar nada)
Port [5432]: (Enter sin ingresar nada)
Username [postgres]: (Enter sin ingresar nada)
Contraseña para usuario postgres: (Ingresar contraseña de postgres)

# Ahora crearemos nuestra base de datos
CREATE DATABASE (Nombre de base de datos);
# Crear Usuario
CREATE USER (Nombre de usuario);
# Cambiar a Base de Datos
\c (Nombre de base de datos)
# Asignar accesos y contraseña
ALTER ROLE (Nombre de Usuario) WITH PASSWORD (Contraseña para usuario entre comillas)
