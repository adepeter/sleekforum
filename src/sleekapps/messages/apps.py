from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MessagesConfig(AppConfig):
    name = 'sleekapps.messages'
    label = 'chats'
    verbose_name = _('Messages')

    def ready(self):
        from . import signals
