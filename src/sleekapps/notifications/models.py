from ..activity.models import Notification as BaseNotification


class Notification(BaseNotification):
    class Meta:
        proxy = True
