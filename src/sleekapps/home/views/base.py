from django.db.models import Q
from django.views.generic import ListView

from ...threads.models import Thread

TEMPLATE_URL = 'home'


class Homepage(ListView):
    model = Thread
    template_name = f'{TEMPLATE_URL}/index.html'
    context_object_name = 'threads'
    paginate_by = 10
    ordering = ['-pin', '-modified']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            Q(pin__gte=2) | ~Q(is_hidden=True)
        ).select_related('starter')

