from django.db import models
from django.db.models import Q


class PrivateMessageManager(models.Manager):
    def correspondence_between(self, sender, recipient):
        return self.filter(
            Q(recipient=recipient, sender=sender) | \
            Q(recipient=sender, sender=recipient)
        )

    def inbox(self, user):
        return self.filter(recipient=user)
