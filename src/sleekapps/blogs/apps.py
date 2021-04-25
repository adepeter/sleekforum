from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = 'sleekapps.blogs'

    def ready(self):
        from . import signals
