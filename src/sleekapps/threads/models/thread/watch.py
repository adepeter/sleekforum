from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ThreadView(models.Model):
    thread = models.ForeignKey(
        'threads.Thread',
        on_delete=models.CASCADE,
        related_name='thread_views'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='thread_views'
    )
    views = models.IntegerField(
        verbose_name=_('Views'),
        default=0,
        help_text=_('View count per thread')
    )
    viewed_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('Viewer')
        verbose_name_plural = _('Viewers')
        constraints = [
            models.UniqueConstraint(
                fields=['thread', 'user'],
                name='unique_thread_user_on_thread_view'
            )
        ]
