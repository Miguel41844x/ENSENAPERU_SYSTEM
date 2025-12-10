"""ASGI config for empresa_educacion project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empresa_educacion.settings")

application = get_asgi_application()
