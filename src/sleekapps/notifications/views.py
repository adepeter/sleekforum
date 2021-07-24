from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _

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
        Notification.objects.filter(user=request.user).update(is_read=True)
        messages.success(request, _('All notifications have been marked as read'))
        return HttpResponseRedirect(reverse('sleekforum:notifications:notifications_list'))
