"""
Django settings for sleekforum project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path, PurePath

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(p%_ifcrc^we&x5!m_-)9#cmtd4ps#tpten*kdh5k8$+t$&b^+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.postgres',
    'django.contrib.redirects',

    # python libraries
    'PIL',

    # django 3rd party apps
    'django_social_share',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'martor',
    'mptt',
    'precise_bbcode',
    'violation',

    # sleekforum apps
    'sleekapps.admin.apps.AdminConfig',
    'sleekapps.ads.apps.AdsConfig',
    'sleekapps.activity.apps.ActivityConfig',
    'sleekapps.blogs.apps.BlogsConfig',
    'sleekapps.categories.apps.CategoriesConfig',
    'sleekapps.cores.apps.CoreConfig',
    'sleekapps.friends.apps.FriendsConfig',
    'sleekapps.home.apps.HomeConfig',
    'sleekapps.graphql.apps.GraphQLConfig',
    'sleekapps.messages.apps.MessagesConfig',
    'sleekapps.notifications.apps.NotificationsConfig',
    'sleekapps.pages.apps.PagesConfig',
    'sleekapps.settings.apps.SettingsConfig',
    'sleekapps.threads.apps.ThreadsConfig',
    'sleekapps.users.apps.UsersConfig',

    # this app extends 3rd party django-violation
    # to provide more features
    'sleekapps.violations.apps.ViolationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',

    # sleekforum custom middleware
    'sleekapps.settings.middlewares.UnderMaintenanceMiddleware',
    'sleekapps.activity.middlewares.LastVisitUpdaterMiddleWare',
    'sleekapps.users.middlewares.FetchCountryFromAPIMiddleware',
    'sleekapps.users.middlewares.OnlineStatusMiddleware',
]

ROOT_URLCONF = 'sleekforum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates' / 'sleekapps'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'string_if_invalid': '%s is not a valid template variable',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # sleekforum context_processors
                'sleekapps.settings.context_processors.site_configuration',
            ],
        },
    },
]

WSGI_APPLICATION = 'sleekforum.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Media files (Uploaded items)
# https://docs.djangoproject.com/en/3.1/howto/media-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = PurePath(BASE_DIR).joinpath('media')

# Locale path for translations
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'graphql_jwt.backends.JSONWebTokenBackend',
    'sleekapps.users.authentication_backend.AuthenticationBackend',
]

AUTH_USER_MODEL = 'users.User'

SITE_ID = 1

GRAPHENE = {
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_ALLOW_ARGUMENT': True,
}

LOGIN_URL = reverse_lazy('sleekforum:users:auth:login')
LOGIN_REDIRECT_URL = reverse_lazy('sleekforum:home:home')
LOGOUT_URL = reverse_lazy('sleekforum:users:auth:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('sleekforum:home:home')

USER_LASTSEEN_TIMEOUT = 60 * 1

# Martor
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',  # to enable/disable emoji icons.
    'imgur': 'true',  # to enable/disable imgur/custom uploader.
    'mention': 'true',  # to enable/disable mention
    'jquery': 'true',  # to include/revoke jquery (require for admin default django)
    'living': 'false',  # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',  # to enable/disable hljs highlighting in preview
}

MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]
