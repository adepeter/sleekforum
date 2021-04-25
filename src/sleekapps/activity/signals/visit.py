import datetime

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from ..models import Visit

today = datetime.datetime.today()


@receiver(user_logged_in)
def update_user_visit(sender, request, user, **kwargs):
    user_visit = Visit.objects.filter(timestamp__date=today)


__all__ = [
    'update_user_visit'
]
