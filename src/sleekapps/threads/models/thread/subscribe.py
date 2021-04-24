from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Subscriber'),
        on_delete=models.CASCADE,
        related_name='subscribed_threads'
    )
    thread = models.ForeignKey(
        'threads.Thread',
        verbose_name=_('Thread'),
        on_delete=models.CASCADE,
        related_name='subscribers'
    )
