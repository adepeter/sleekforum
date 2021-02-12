from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('sender'),
        on_delete=models.DO_NOTHING,
        related_name='messages_sent'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('sender'),
        on_delete=models.DO_NOTHING,
        related_name='messages_received'
    )
    content = models.TextField(
        verbose_name=_('content'),
    )
    is_read = models.BooleanField(
        verbose_name=_('is read'),
        default=False,
    )
    date_sent = models.DateTimeField(
        verbose_name=_('date sent'),
        auto_now_add=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent message'),
        on_delete=models.PROTECT,
        related_name='children'
    )
