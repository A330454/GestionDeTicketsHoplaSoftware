from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

# Establece la configuración por defecto de Django para el módulo de Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_management.settings')

app = Celery('ticket_management')

# Usar una cadena para que el trabajador no tenga que serializar
# el objeto de configuración al usar Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todos los módulos registrados en aplicaciones configuradas.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Configuración de logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
