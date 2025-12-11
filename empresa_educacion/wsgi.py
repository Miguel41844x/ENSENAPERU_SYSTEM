"""WSGI config for empresa_educacion project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empresa_educacion.settings")

application = get_wsgi_application()
