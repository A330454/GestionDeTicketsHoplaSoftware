# 🌟 Gestión De Tickets Hoplasoftware

📝 Este proyecto es una api rest que nos permita gestionar los tickets de creación de transacciones en una aplicación de subida de fotos.

## 📋 Requisitos Previos

- **Python** 🐍: Asegúrate de tener Python 3.11.5 o superior instalado.
- **Editor de Código** 💻: Recomendamos Visual Studio Code o PyCharm para una experiencia de desarrollo óptima.

### Instalación 🔧

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
(nombreDelEntorno) D:\proyectos-programacion\flask\Ejemplo> 
```

Ahora diríjete a la carpeta del proyecto desde tu consola CMD y una vez dentro, te darás cuenta que existe el archivo requirements.txt, en la misma altura de este archivo, es decir, que si damos el comando "dir" podamos verlo en los archivos que se registran en consola, hay que dar el siguiente comando

```cmd
(nombreDelEntorno) D:\proyectos-programacion\flask\Ejemplo\ProyectoChingon123> pip install -r requirements.txt 
```

Este comando descargará todas las dependencias que el proyecto necesita, es importante que cada vez que se instale una dependencia nueva en el proyecto, actualicemos el archivo requirements.txt para no tene problemas con dependencias o versiones futuras de nuestro proyecto
  
## 🛠️ Comandos de Proyecto con Django

🔥 Para iniciar el servidor de desarrollo, navega a la carpeta del proyecto y ejecuta:
  ```bash
    python manage.py runserver
  ```

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
