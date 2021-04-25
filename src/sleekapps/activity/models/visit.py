from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..managers.visits import VisitManager


class Visit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='user_visits',
        unique_for_date='timestamp'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    objects = VisitManager()

    def __str__(self):
        return f'Visit for {self.user.username} at {self.timestamp} was succesfully created'
