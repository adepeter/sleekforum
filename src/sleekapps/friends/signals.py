from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FriendRequest


@receiver(post_save, sender=FriendRequest)
def friend_request_notification(sender, instance, created, **kwargs):
    pass
