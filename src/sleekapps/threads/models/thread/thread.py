from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


from ...managers.thread import ThreadManager
from ...modelurls.thread import ThreadModelURL

limit_choices_to = models.Q(is_lock=False)


class Thread(models.Model, ThreadModelURL):
    PIN_DEFAULT = 0
    PIN_LOCALLY = 1
    PIN_GLOBALLY = 2

    PREFIX_DEFAULT = 0
    PREFIX_HELP = 1
    PREFIX_DISCUSSION = 2
    PREFIX_INFO = 3

    PREFIX_CHOICES = (
        (PREFIX_DEFAULT, _('Default')),
        (PREFIX_HELP, _('Help')),
        (PREFIX_DISCUSSION, _('Discussion')),
        (PREFIX_INFO, _('Info')),
    )

    PIN_CHOICES = (
        (PIN_DEFAULT, _('Do not pin thread')),
        (PIN_LOCALLY, _('Pin thread within category')),
        (PIN_GLOBALLY, _('Pin thread globally')),
    )

    starter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('starter'),
        on_delete=models.SET_NULL,
        related_name='threads',
        null=True
    )
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        related_name='threads',
        limit_choices_to=limit_choices_to
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=150,
        unique=True
    )
    tags = ArrayField(
        models.CharField(max_length=30),
        blank=True,
        null=True,
        size=8,
        help_text=_('Thread tags separated by comma')
    )
    pin = models.IntegerField(
        verbose_name=_('pin thread'),
        choices=PIN_CHOICES,
        default=PIN_DEFAULT
    )
    prefix = models.IntegerField(
        verbose_name=_('prefix'),
        choices=PREFIX_CHOICES,
        default=PREFIX_DEFAULT
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True,
        editable=False
    )
    content = models.TextField(
        verbose_name=_('content'),
        unique_for_date='created'
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_locked = models.BooleanField(
        verbose_name=_('lock thread'),
        default=False
    )
    is_hidden = models.BooleanField(
        verbose_name=_('hide thread'),
        default=False
    )
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    sads = models.PositiveIntegerField(default=0)
    happies = models.PositiveIntegerField(default=0)
    wows = models.PositiveIntegerField(default=0)
    angries = models.PositiveIntegerField(default=0)
    funnies = models.PositiveIntegerField(default=0)
    loves = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    reactions = GenericRelation(
        'activity.Reaction',
        related_query_name='threads'
    )
    violations = GenericRelation(
        'violation.Violation',
        related_query_name='threads'
    )

    objects = ThreadManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.tags = [slugify(tag) for tag in self.tags]
        super().save(*args, **kwargs)

    def get_reaction_count(self, reaction):
        return self.reactions.filter_reaction_by(reaction).count()

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(
                fields=['id', 'slug'],
                name='idx_id_slug_on_thread'
            )
        ]
        ordering = ['-modified']
