# Tehnical_test AHT

## Descripción

Este proyecto es una aplicación web desarrollada en Flask que permite a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos MySQL. Utiliza SQLAlchemy para interactuar con la base de datos y está dockerizada para facilitar su ejecución en un entorno independiente.

## Prerrequisitos

- Python (versión 3.x)
- Docker instalado y configurado en el sistema
- Librerías necesarias:
  - Flask: un marco de trabajo para desarrollar aplicaciones web en Python.
  - SQLAlchemy: un ORM (Object Relational Mapper) para interactuar con bases de datos.
  - Jinja2: un motor de plantillas para renderizar HTML con Python.

## Instrucciones para ejecutar la aplicación

1.  Clona el repositorio** en tu máquina local:
   git clone <URL del repositorio>
   cd tecnical_aht
2. **Construye y ejecuta los contenedores** usando Docker Compose:
    docker-compose up --build
    Si haces cambios reconstruye la imagen con:
    docker-compose up -d
3. **Accede a la aplicación** en tu navegador en http://localhost:5000.
4. **Asegúrate de que el puerto 3307 no esté en uso** antes de ejecutar la aplicación.
5. La base de datos MySQL estará disponible en el puerto 3307 en tu máquina local. Si necesitas conectarte a ella desde otro servicio, utiliza localhost:3307.