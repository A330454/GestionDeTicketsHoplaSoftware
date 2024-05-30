from __future__ import absolute_import, unicode_literals

# Esto asegurará que se cargue la configuración de Celery cuando se ejecute Django.
from .celery import app as celery_app

__all__ = ('celery_app',)