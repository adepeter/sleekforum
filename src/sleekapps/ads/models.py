from django.db import models
from django.utils.translation import gettext_lazy as _


class Advertisement(models.Model):
    name = models.CharField(
        verbose_name=_('ADS Name'),
        max_length=50
    )
    link = models.URLField(
        verbose_name=_('URL of ADS'),
        default='https://',
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
