"""
ASGI config for sleekforum project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
sleekforum_environment = os.environ.get('SLEEKFORUM_ENVIRONMENT', 'sleekforum.settings.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', sleekforum_environment)

application = get_asgi_application()
