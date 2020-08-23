import os

from ._base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SLEEKFORUM_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('SLEEKFORUM_DB_NAME', 'sleekforum_db'),
        'USER': os.environ.get('SLEEKFORUM_DB_USER', 'sleekforum_user'),
        'PASSWORD': os.environ.get('SLEEKFORUM_DB_PASSWORD', 'sleekforum_password'),
        'HOST': os.environ.get('SLEEKFORUM_DB_HOST', 'localhost'),
        'PORT': os.environ.get('SLEEKFORUM_DB_PORT', '5432')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')