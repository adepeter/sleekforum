from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        editable=False,
        blank=True
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True
    )
    is_locked = models.BooleanField(
        verbose_name=_('Lock'),
        default=True,
        help_text=_('If locked, users cannot see add post or \
        make alteration to articles/posts in this category totally')
    )
    is_hidden = models.BooleanField(
        verbose_name=_('Hide'),
        default=False,
        help_text=_('If hidden, users cannot see article in this category totally')
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
