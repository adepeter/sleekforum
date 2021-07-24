from django.db import models
from django.db.models import Q


class PrivateMessageManager(models.Manager):
    def correspondence_between(self, sender, recipient):
        return self.filter(
            Q(recipient=recipient, sender=sender) | \
            Q(recipient=sender, sender=recipient)
        )

    def inbox(self, user, read_status=None):
        return self.filter(
            recipient=user, is_read=read_status is not None and not False
        )
