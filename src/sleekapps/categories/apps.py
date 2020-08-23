from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    name = 'sleekapps.categories'

    def ready(self):
        from . import signals
