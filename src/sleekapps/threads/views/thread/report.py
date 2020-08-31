from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from violation.views.violation import BaseViolationView

from ...forms.thread.violation import ThreadReportForm
from ...models import Thread

TEMPLATE_URL = 'threads/thread'


class ReportThread(SuccessMessageMixin, BaseViolationView):
    model = Thread
    form_class = ThreadReportForm
    success_message = _('Your report was successfully submitted for reviewal by an admin')
    query_pk_and_slug = True
    template_name = f'{TEMPLATE_URL}/report_thread.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form.fields['rules'])
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.get_object()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['object'] = self.get_object()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        instance = form.save()
        instance.rules.set(form.cleaned_data['rules'])
        return super().form_valid(form)

    def get_success_url(self):
        thread = self.get_object()
        return thread.get_absolute_url()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug__iexact=self.kwargs['category_slug'])
