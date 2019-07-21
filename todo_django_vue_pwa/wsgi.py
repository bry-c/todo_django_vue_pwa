"""
WSGI config for todo_django_vue_pwa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_django_vue_pwa.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
