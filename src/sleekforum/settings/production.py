import os

from ._base import *

DEBUG = False

ALLOWED_HOSTS = ['sleekforum.com', 'www.sleekforum.com']

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

# Caching
# https://docs.djangoproject.com/en/3.1/topics/cache/#setting-up-the-cache

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True