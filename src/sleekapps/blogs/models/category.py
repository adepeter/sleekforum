from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        on_delete=models.DO_NOTHING,
        related_name='owned_blog_categories'
    )
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
    icon = models.ImageField(
        verbose_name='image',
        upload_to='blogs/categories/icons',
        blank=True
    )
    cover = models.ImageField(
        verbose_name='cover',
        upload_to='blogs/categories/covers',
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
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} by {self.owner.get_display_name}'
    
    class Meta:
        verbose_name_plural = _('categories')
