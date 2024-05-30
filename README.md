# 📝 Gestión De Tickets Hoplasoftware

Este proyecto es una api rest que nos permita gestionar los tickets de creación de transacciones en una aplicación de subida de fotos.

## Endpoints
Esto es una breve introducción a los endpoints que encontrarás en este proyecto. Podrás encontrar más información una ves ejecutes el proyecto en http://127.0.0.1:8000/swagger/ (generación de documentación automática con Swagger)

- **Create Ticket**: http://127.0.0.1:8000/api/tickets/create/


Payload: {"num_images": 3, "status":"pending"}
- **Upload Image**: http://127.0.0.1:8000/api/tickets/upload/


Payload: {"ticket": 1, "image_url": "https://t4.ftcdn.net/jpg/01/43/23/83/360_F_143238306_lh0ap42wgot36y44WybfQpvsJB5A1CHc.jpg"}

  Nota: el campo ticket en el payload es el ID de el ticket existente
- **List Tickets**: http://127.0.0.1:8000/api/tickets/upload/](http://127.0.0.1:8000/api/tickets/list/
- **List Tickets por status**: http://127.0.0.1:8000/api/tickets/list/?status=completed
- **List Tickets por dia**: http://127.0.0.1:8000/api/tickets/list/?start_date=2024-05-29&end_date=2024-05-31
- **List Tickets por dia y por status**: http://127.0.0.1:8000/api/tickets/list/?start_date=2024-05-29&end_date=2024-05-31&status=pending
- **List Tickets por dia y por status**: http://127.0.0.1:8000/api/tickets/detail/{id}
- **Image Detail**: http://127.0.0.1:8000/api/tickets/image/{id}


## 📋 Requisitos Previos

- **Python** 🐍: Asegúrate de tener Python 3.11.5 o superior instalado.
- **Editor de Código** 💻: Recomendamos Visual Studio Code o PyCharm para una experiencia de desarrollo óptima.

## 🔧 Instalación 

Una ves hayas clonado el proyecto en tu maquina local el primer paso sería tomar el archivo Redis-x64-3.0.504.zip, ir a la raíz de tu equipo (C:) y crear la carpeta \Redis, una vez que estemos dentro de C:\Redis y descomprimos el archivo, esto nos permitirá ejecutar redis nuestro cmdde la siguiente manera.

```cmd
> redis-server.exe
```

Fuera de la carpeta del proyecto en tu consola ejecuta el siguente comando para crear un entorno virtual de python (Asegúrate de tener instalado Python para este paso).

```cmd
> py -m venv nombreDelEntorno
```

luego accede a la nueva carpeta con el nombre que elegiste para tu entorno y accede a la carpeta scripts y activa el entorno con los siguientes comandos

```cmd
> cd nombreDelEntorno
> cd scripts
> activate
```

Verás como se activa porque se ve el nombre del entorno entre parentesis en tu consola

```cmd
(nombreDelEntorno) D:\proyectos-programacion\venv\scripts\activate>
```

Ahora diríjete a la carpeta del proyecto desde tu consola CMD y una vez dentro, te darás cuenta que existe el archivo requirements.txt, en la misma altura de este archivo, es decir, que si damos el comando "dir" podamos verlo en los archivos que se registran en consola, hay que dar el siguiente comando

```cmd
(nombreDelEntorno) D:\proyectos-programacion\ticket_management> pip install -r requirements.txt 
```

Este comando descargará todas las dependencias que el proyecto necesita, es importante que cada vez que se instale una dependencia nueva en el proyecto, actualicemos el archivo requirements.txt para no tene problemas con dependencias o versiones futuras de nuestro proyecto
  
## 🛠️ Ejecución del Proyecto

Se requiere tener 3 terminales activas para el funcionamiento correcto de este proyecto, esto para levantar el servicio de redis, de celery y de Django para su trabajo en conjunto.

Primero que nada, una vez actives tu venv realiza las migraciones de la base de datos.
```bash
    python manage.py makemigrations
    python manage.py migrate
  ```

 Para iniciar el servidor de desarrollo, navega a la carpeta del proyecto con el venv activo y ejecuta:
  ```bash
    (nombreDelEntorno) D:\proyectos-programacion\ticket_management>py manage.py runserver
  ```

 Abrimos una términal de CMD y ejecutamos el sigueinte comando para levantar el servicio de redis.
  ```bash
    redis-server.exe
  ```

Activamos el venv, navegamos a la carpeta del proyecto y ejecutamos.
  ```bash
    (nombreDelEntorno) D:\proyectos-programacion\ticket_management>celery -A ticket_management worker --loglevel=info
  ```

## 🛠️ Comandos comunes de Django

📦 Creación de aplicaciones

  ```bash
    python manage.py startapp nombre_de_la_app
  ```

📚 Configuración de la Base de Datos y Migraciones
- No olvides configurar tu base de datos en *settings.py* y realizar las migraciones:

  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```

👤 Crea un superusuario para el administrador de Django:
  ```bash
    python manage.py createsuperuser
  ```
## Autor ✒️

* **Jacobo Espino De Alba** - [Github](https://github.com/A330454)
