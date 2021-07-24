from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import Signal, receiver

from .models import PrivateMessage
from .views import ReadReplyPrivateMessage

is_read_handler = Signal()


@receiver(is_read_handler, sender=ReadReplyPrivateMessage)
def mark_is_read_for_both(sender, **kwargs):
    request = kwargs.get('request')
    messages = kwargs.get('messages')
    try:
        last_message = messages.latest()
        if last_message.recipient == request.user:
            messages.update(is_read=True)
    except ObjectDoesNotExist:
        pass


@receiver(pre_save, sender=PrivateMessage)
def prevent_multi_chat(sender, instance, **kwargs):
    sender = instance.sender
    recipient = instance.recipient
    correspondence = PrivateMessage.objects.correspondence_between(sender, recipient)
    if correspondence.exists():
        instance.parent = correspondence.first()
