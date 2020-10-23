from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

from ..models import Reaction


@receiver(pre_save, sender=Reaction)
def reaction_updater(sender, instance, **kwargs):
    ct = ContentType.objects.get_for_model(instance.content_object)
    obj = ct.get_object_for_this_type(id=instance.object_id)
    reaction = Reaction.objects.filter(
        user=instance.user,
        content_type=ct,
        object_id=obj.id
    )