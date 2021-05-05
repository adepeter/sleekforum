from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sleekapps.admin'
    verbose_name = 'SleekForum Admin'
    label = 'sleekforum_admin'
