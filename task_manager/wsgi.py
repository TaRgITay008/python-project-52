import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

application = get_wsgi_application()

# Rollbar
import rollbar
from django.conf import settings

rollbar.init(
    access_token=settings.ROLLBAR['access_token'],
    environment=settings.ROLLBAR['environment'],
    branch=settings.ROLLBAR['branch'],
    root=settings.ROLLBAR['root'],
)
