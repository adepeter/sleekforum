from django.db import models
from django.utils.translation import gettext_lazy as _

from .behaviours import Configuration


class Setting(Configuration):
    title = models.CharField(
        verbose_name=_('site title'),
        max_length=20,
        help_text=_('website title')
    )
    email = models.EmailField(
        verbose_name=_('e-mail'),
        default='noreply@localhost',
    )
    welcome_mail = models.TextField(
        verbose_name=_('welcome message'),
        help_text=_('message after successful registration'),
        blank=True
    )
    allow_registration = models.BooleanField(default=True)
    captcha = models.BooleanField(default=False, help_text=_('Turn on/off captcha on pages'))
    threads_per_page = models.PositiveSmallIntegerField(default=10)
    posts_per_thread = models.PositiveSmallIntegerField(default=10)
