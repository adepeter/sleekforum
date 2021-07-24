# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Notification

TEMPLATE_URL = 'notifications'


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = f'{TEMPLATE_URL}/notifications_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
