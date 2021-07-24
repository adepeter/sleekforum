from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..behaviours import ActivityStreamMixin


class Notification(ActivityStreamMixin):
    action_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Action performed by'),
        on_delete=models.CASCADE,
        related_name='notifications',
        help_text=_('User who triggered the notifications action')
    )
    alert = models.TextField()
    is_read = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
