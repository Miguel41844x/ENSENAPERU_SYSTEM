# ENSENAPERU_SYSTEM

Proyecto base en **Django** para la gestión de una empresa de educación, preparado para conectarse a una base de datos **Oracle** y con una plantilla inicial editable.

## Requisitos
- Python 3.11+
- Dependencias Python: ver `requirements.txt` (Django y `oracledb` para Oracle). Si no puedes instalar paquetes por restricciones de red, descarga las ruedas previamente o usa un mirror interno.
- Cliente de Oracle instalado o accesible en el servidor donde se ejecute el proyecto.

## Configuración de entorno
Crea un archivo `.env` (o variables de entorno equivalentes) con los valores de conexión y ajustes básicos:

```
DJANGO_SECRET_KEY="cambia-este-valor"
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=XE
ORACLE_USER=system
ORACLE_PASSWORD=oracle
```

## Puesta en marcha
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Aplica migraciones:
   ```bash
   python manage.py migrate
   ```
3. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

La ruta `/` muestra la plantilla editable (`templates/base.html`) y `/admin/` abre el panel de administración estándar de Django.

## Estructura relevante
- `manage.py`: utilidades de línea de comandos de Django.
- `empresa_educacion/settings.py`: configuración general y conexión a Oracle.
- `empresa_educacion/urls.py`: rutas principales; carga la plantilla base como página de inicio.
- `templates/base.html`: plantilla editable lista para personalizar con información de cursos, instructores y alumnos.
