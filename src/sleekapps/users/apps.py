from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'sleekapps.users'

    def ready(self):
        from . import signals
