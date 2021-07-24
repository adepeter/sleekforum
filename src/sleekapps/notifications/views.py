from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
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


class MarkAllAsRead(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        Notification.objects.filter(user=request.user)
        print(self.request.user)
        from django.http import HttpResponse
        return HttpResponse('<b>Hello!</b>')
