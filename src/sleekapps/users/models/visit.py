from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Visit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='visits'
    )
    visit_record = models.DateTimeField()

    def __str__(self):
        return f'Last visit for {self.user} was {self.visit_record}'

    class Meta:
        ordering = ['-visit_record']
        get_latest_by = 'visit_record'
