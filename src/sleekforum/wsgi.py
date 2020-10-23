"""
WSGI config for sleekforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
sleekforum_environment = os.environ.get('SLEEKFORUM_ENVIRONMENT', 'sleekforum.settings.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', sleekforum_environment)

application = get_wsgi_application()
