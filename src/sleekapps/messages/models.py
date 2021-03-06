from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import PrivateMessageManager


class PrivateMessage(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('sender'),
        on_delete=models.DO_NOTHING,
        related_name='messages_sent'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('recipient'),
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
        related_name='children',
        null=True,
        blank=True
    )
    objects = PrivateMessageManager()

    def get_absolute_url(self):
        kwargs = {
            'id': self.recipient.id,
            'username': self.recipient.username
        }
        return reverse('sleekforum:messages:read_reply_private_message', kwargs=kwargs)

    def __str__(self):
        return f'{self.sender.username} correspondence with {self.recipient.username} - {self.content}'

    class Meta:
        ordering = [
            'id'
        ]
        get_latest_by = 'date_sent'


class Message(PrivateMessage):
    class Meta:
        proxy = True


class Chat(PrivateMessage):
    class Meta:
        proxy = True


class PrivateChat(PrivateMessage):
    class Meta:
        proxy = True
