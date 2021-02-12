from django.views.generic import ListView

from .models import PrivateMessage


class ListPrivateMessage(ListView):
    model = PrivateMessage
