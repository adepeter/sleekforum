import readtime
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    MARK_DRAFT = 0
    MARK_COMPLETED = 1

    COMPLETION_STATUS_CHOICES = (
        (MARK_DRAFT, _('draft')),
        (MARK_COMPLETED, _('completed'))
    )

    category = models.ForeignKey(
        'blogs.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        related_name='articles'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='blog_articles',
        null=True
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
    )
    cover = models.ImageField(
        verbose_name=_('cover image'),
        upload_to='blogs/covers',
        blank=True
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        editable=False,
        blank=True
    )
    tags = ArrayField(
        models.CharField(max_length=30),
        blank=True,
        null=True,
        size=8,
        help_text=_('Thread tags separated by comma')
    )
    content = models.TextField(
        verbose_name='article body',
        blank=True,
        null=True,
        help_text=_('If content is not entered, its marked as draft')
    )
    completion_status = models.IntegerField(
        verbose_name=_('completion Status'),
        choices=COMPLETION_STATUS_CHOICES,
        default=MARK_DRAFT,
        editable=False,
        help_text=_('Choose status of blog default is DRAFT')
    )
    is_locked = models.BooleanField(
        verbose_name=_('Lock'),
        default=True
    )
    is_hidden = models.BooleanField(
        verbose_name=_('Hide'),
        default=False
    )
    date_created = models.DateTimeField(
        verbose_name=_('Date created'),
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        verbose_name=_('Date modified'),
        auto_now=True
    )

    def get_read_time(self):
        return readtime.of_text(self.content)

    def get_absolute_url(self):
        kwargs = {
            'id': self.id,
            'slug': self.slug,
            'username': self.author.username
        }
        return reverse('sleekforum:blogs:articles:user_read_article', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
