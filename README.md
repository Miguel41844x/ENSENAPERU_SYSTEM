# ENSEÑA PERÚ SYSTEM

Aplicación web en **Django** para administrar procesos académicos de Enseña Perú: gestión de cuentas, estudiantes, voluntarios, evaluaciones, asignaciones y escuelas. Incluye configuración lista para usar **Oracle** como base de datos y plantillas iniciales para personalizar la interfaz.

## Requisitos previos
- Python 3.11 o superior.
- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) instalado en el host donde se ejecutará la aplicación.
- Acceso a una instancia Oracle accesible por red.
- Dependencias Python listadas en `requirements.txt`.

## Instalación y configuración
1. Clona el repositorio y crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. Crea un archivo `.env` (o exporta variables de entorno equivalentes) con tus credenciales y ajustes básicos:
   ```env
   DJANGO_SECRET_KEY="cambia-este-valor"
   DJANGO_DEBUG=true
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

   # Credenciales Oracle
   ORACLE_DSN=localhost:1521/FREEPDB1
   ORACLE_USER=system
   ORACLE_PASSWORD=oracle
   ```
3. Aplica migraciones y crea un usuario administrador:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
   - `/` muestra la plantilla base inicial.
   - `/admin/` abre el panel de administración estándar de Django.

## Configuración relevante
- **Base de datos:** definida en `empresa_educacion/settings.py` usando `django.db.backends.oracle` y las variables `ORACLE_DSN`, `ORACLE_USER` y `ORACLE_PASSWORD`.
- **Zona horaria e idioma:** configurados como `America/Lima` y `es-es` respectivamente.
- **Archivos estáticos:** se sirven desde `static/` en desarrollo y se recolectan en `staticfiles/` para despliegues.
- **Autenticación:** URLs de inicio/cierre de sesión apuntan a `login`, `dashboard` y `logout` definidos en las vistas de las apps.

## Estructura principal
- `manage.py`: utilidades de línea de comandos de Django.
- `empresa_educacion/`: configuración general del proyecto (URLs, settings, ASGI/WSGI).
- `accounts/`, `assignments/`, `evaluations/`, `students/`, `volunteers/`, `escuelas/`, `core/`: aplicaciones Django que encapsulan la lógica de negocio.
- `templates/`: plantilla base (`base.html`) y otras vistas HTML reutilizables.
- `static/`: recursos estáticos (CSS, JS, imágenes) para la interfaz.

## Comandos útiles
- Levantar el servidor en otro puerto: `python manage.py runserver 0.0.0.0:8080`
- Revisar problemas de configuración: `python manage.py check`
- Recolectar archivos estáticos para despliegue: `python manage.py collectstatic`

## Notas para despliegue
- Define `DJANGO_DEBUG=false` y ajusta `DJANGO_ALLOWED_HOSTS` con los dominios públicos.
- Configura un servidor WSGI o ASGI (uWSGI, Gunicorn, Daphne) detrás de un proxy inverso (Nginx/Apache).
- Revisa que `ORACLE_DSN` apunte al servicio/PDB correcto y que el cliente Oracle esté disponible en tiempo de ejecución.
- Ejecuta `collectstatic` y sirve los archivos de `staticfiles/` desde tu servidor web o CDN.
