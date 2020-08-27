from django.db import models
from django.utils.translation import gettext_lazy as _

from ...cores.utils.choice import Choicify

from ..behaviours import ActivityStreamMixin
from ..constants import REACTION_CHOICES
from ..managers.reaction import ReactionManager

reaction_choices = Choicify(REACTION_CHOICES)


class Reaction(ActivityStreamMixin):
    reaction = models.CharField(
        verbose_name=_('Reaction'),
        max_length=len(reaction_choices),
        choices=reaction_choices.get_choices
    )

    objects = ReactionManager()

    class Meta:
        verbose_name_plural = _('Reactions')
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'reaction', 'content_type', 'object_id'],
                name='unique_user_activity'
            )
        ]