from django.contrib.contenttypes.models import ContentType
from django.db import models


class ReactionManager(models.Manager):

    def filter_reaction_by(self, reaction, obj=None):
        if obj is not None:
            return self.filter(
                content_type=ContentType.objects.get_for_model(obj),
                reaction__iexact=reaction,
                object_id=obj.id
            )
        return self.filter(reaction=reaction)