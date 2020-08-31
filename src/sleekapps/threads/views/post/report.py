from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from violation.views.violation import BaseViolationView

from ...forms.post.report import PostReportForm
from ...viewmixins.post import BasePostMixin

from ...models import Post

TEMPLATE_URL = 'threads/post'


class ReportPost(SuccessMessageMixin, BasePostMixin, BaseViolationView):
    model = Post
    form_class = PostReportForm
    success_message = _('Your report was successfully submitted for reviewal by an admin')
    query_pk_and_slug = True
    template_name = f'{TEMPLATE_URL}/report_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
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
        post = self.get_object()
        return post.get_absolute_url()
