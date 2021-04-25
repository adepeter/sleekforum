from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('poster'),
        on_delete=models.SET_NULL,
        related_name='blog_comments',
        null=True
    )
    article = models.ForeignKey(
        'blogs.Article',
        verbose_name=_('article'),
        on_delete=models.CASCADE,
        related_name='blog_comments'
    )
    content = models.TextField(
        verbose_name='comment body',
        blank=True
    )
    is_hidden = models.BooleanField(
        verbose_name=_('hide'),
        default=False
    )
    date_posted = models.DateTimeField(
        verbose_name=_('date posted'),
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        verbose_name=_('date modified'),
        auto_now=True
    )
