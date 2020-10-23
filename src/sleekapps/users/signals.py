from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .utils import ImageHandler

avatar = ImageHandler()

@receiver(post_save, sender=User)
def link_default_avatar(sender, instance, created, **kwargs):
    if created:
        instance.avatar = avatar.get_avatar(instance)
        instance.save()