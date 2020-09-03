from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from ...managers.post import PostManager
from ...modelurls.post import PostModelURL


class Post(models.Model, PostModelURL):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('post'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    thread = models.ForeignKey(
        'threads.Thread',
        verbose_name=_('thread'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    reactions = GenericRelation(
        'activity.Reaction',
        related_query_name='posts'
    )
    violations = GenericRelation(
        'violation.Violation',
        related_query_name='posts'
    )
    content = models.TextField(verbose_name=_('Post content'))
    is_hidden = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(verbose_name=_('likes'), default=0)
    dislikes = models.PositiveIntegerField(
        verbose_name=_('dislikes'),
        default=0
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='children',
        null=True,
        blank=True
    )

    objects = PostManager()

    def __str__(self):
        return f'{self.content[:10]} by {self.user.username} to {self.thread.title}'

    class Meta:
        verbose_name = _('Post')
        ordering = ['created']
        verbose_name_plural = _('Posts')
        get_latest_by = 'created'
