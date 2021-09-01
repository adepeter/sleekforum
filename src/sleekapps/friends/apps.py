from django.apps import AppConfig


class FriendsConfig(AppConfig):
    name = 'sleekapps.friends'

    def ready(self):
        from . import signals
