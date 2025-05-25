[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_ZN33GSt)
# Taller Inicial de Django: Views y Templates

Este laboratorio está diseñado para que los participantes puedan aprender y reforzar sus conocimientos de Python, HTML y CSS mediante la creación de una lista de Pokemones y una página de datalle. Utilizando como framework de desarrollo MVC a Django. De la misma manera se hará una introduccion a Bootstrap para el uso de librerías de Interfaz de usuario en HTML.


## Objetivo
El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) como: Clases, Ojetos, Atributos, Métodos. Así mismo el presente proyecto introduce al desarrollo de aplicaciones Web mediante el uso de Django como marco de trabajo para el desarrollo.

## Tareas a realizar
1. Crear la aplicación para la gestión de Pokemones
2. Crear la página inicial
3. Crear la página de detalles

## Instalación del ambiente
### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Iniciar el servidor

Para inicial el servidor se debe activar el ambiente virtual (revisar paso anterior) ejecutar el siguiente comando

### Linux o MaCOS
~~~
python3 manage.py runserver
~~~
### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

## Crear nueva aplicación

Para generar la primera aplicación se deberá ejecutar el siguiente comando

### Linux o MaCOS
~~~
python3 manage.py startapp pokedex
~~~
### Windows
~~~
python manage.py startapp pokedex
~~~

Para los siguientes pasos se deberán seguir las instrucciones del docente en clase. No olvide que puedes contactarlo a <pablo.perez@uisek.edu.ec> o <paperez@puce.edu.ec> para consultar cualquier inquietud del presente laboratorio
