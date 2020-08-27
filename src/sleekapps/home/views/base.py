from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext_lazy as _

from ...threads.models import Thread

from ..forms.base import HomepageThreadCreationForm

TEMPLATE_URL = 'home'


class Homepage(MultipleObjectMixin, SuccessMessageMixin, CreateView):
    model = Thread
    template_name = f'{TEMPLATE_URL}/index.html'
    paginate_by = 3
    ordering = ['-pin', '-modified']
    form_class = HomepageThreadCreationForm
    success_message = _('%(title)s was successfully created')

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        msg = _("There is an error with the thread you're trying to create.")
        messages.error(self.request, msg)
        return super().form_invalid(form)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            Q(pin__gte=2) | ~Q(is_hidden=True)
        ).select_related('starter')