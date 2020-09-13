from django.db import models
from django.utils.translation import gettext_lazy as _

from .behaviours import Configuration


class Setting(Configuration):
    title = models.CharField(
        verbose_name=_('site title'),
        max_length=20,
        help_text=_('Website title')
    )
    description = models.TextField(
        verbose_name=_('site description'),
        blank=True,
        help_text=_('Website metatag description contents')
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
    is_under_maintenance = models.BooleanField(
        verbose_name=_('maintenance status'),
        default=False,
        help_text=_('Determine if site is under maintenance')
    )
    send_welcome_mail = models.BooleanField(
        verbose_name=_('send welcome email'),
        default=False,
        help_text=_('Send welcome mail to new users')
    )
    allow_registration = models.BooleanField(default=True)
    captcha = models.BooleanField(
        verbose_name=_('captcha verification'),
        default=False,
        help_text=_('Turn on/off captcha on pages')
    )
    threads_per_page = models.PositiveSmallIntegerField(
        verbose_name=_('threads on a page'),
        default=10,
        help_text=_('Number of threads to show on a page')
    )
    posts_per_thread = models.PositiveSmallIntegerField(
        verbose_name=_('posts per thread'),
        default=10,
        help_text=_('Number of posts to display per thread')
    )
