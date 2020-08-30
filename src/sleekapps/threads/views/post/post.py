from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.translation import gettext_lazy as _

from ...forms.post.post import PostEditForm, PostForm
from ...viewmixins.post import BasePostMixin

TEMPLATE_URL = 'threads/post'


class EditPost(BasePostMixin, UpdateView):
    form_class = PostEditForm
    template_name = f'{TEMPLATE_URL}/edit_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        if not form.has_changed():
            messages.success(self.request, _('No changes were made to your reply'))
        else:
            messages.success(self.request, _('Post was successfully edited.'))
        return super().form_valid(form)


class DeletePost(BasePostMixin, DeleteView):
    pass


class ReplyPost(BasePostMixin, CreateView):
    form_class = PostForm
    template_name = f'{TEMPLATE_URL}/reply_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent'] = self.get_object()
        return context

    def form_valid(self, form):
        parent_object = self.get_object()
        form.instance.thread = parent_object.thread
        form.instance.parent = parent_object
        form.instance.user = self.request.user
        return super().form_valid(form)