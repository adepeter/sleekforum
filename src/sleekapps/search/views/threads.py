from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from ...threads.models import Thread

TEMPLATE_URL = 'search/threads'

class CategoryThreadSearch:
    pass

class GlobalThreadSearch(FormMixin, ListView):
    model = Thread
    paginate_by = 10
    template_name = f'{TEMPLATE_URL}/search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search_thread'):
            pass
        return qs.none()