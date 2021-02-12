from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, CreateView

from .forms import PrivateMessageReplyForm
from .models import PrivateMessage

TEMPLATE_URL = 'messages'

User = get_user_model()


class ListPrivateMessage(ListView):
    model = PrivateMessage
    template_name = f'{TEMPLATE_URL}/private_messages.html'


class ReadReplyPrivateMessage(LoginRequiredMixin, CreateView):
    model = User
    form_class = PrivateMessageReplyForm
    template_name = f'{TEMPLATE_URL}/start_private_message.html'
    query_pk_and_slug = True
    slug_url_kwarg = 'username'

    def get_slug_field(self):
        return str('username__iexact')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['recipient'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        recipient = self.get_object()
        form.instance.recipient = recipient
        form.instance.content = form.cleaned_data['content']
        form.instance.sender = self.request.user
        msg = PrivateMessage.objects.filter(
            Q(sender=self.request.user, recipient=recipient) | \
            Q(sender=recipient, recipient=self.request.user),
            parent__isnull=True
        )
        if msg.exists():
            msg = msg.first()
            form.instance.parent = msg
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'recipient': self.get_object(),
            'sender': self.request.user
        })
        return kwargs
