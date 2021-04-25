from django.apps import AppConfig


class ActivityConfig(AppConfig):
    name = 'sleekapps.activity'

    def ready(self):
        from . import signals
