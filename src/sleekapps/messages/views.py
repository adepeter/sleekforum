from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.list import MultipleObjectMixin

from .forms import PrivateMessageReplyForm
from .models import PrivateMessage

TEMPLATE_URL = 'messages'

User = get_user_model()


class ListPrivateMessage(ListView):
    model = PrivateMessage
    context_object_name = 'private_messages'
    template_name = f'{TEMPLATE_URL}/private_messages.html'
    ordering = ['is_read', 'date_sent']

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(parent__isnull=True)
        return qs


class ReadReplyPrivateMessage(LoginRequiredMixin, MultipleObjectMixin, CreateView):
    model = User
    form_class = PrivateMessageReplyForm
    template_name = f'{TEMPLATE_URL}/start_private_message.html'
    context_object_name = 'private_messages'
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        from .signals import is_read_handler
        """
        Uncomment the below block if you want to restrict user from sending message to self.
        Although, this has been enforced at form_class and template level.
        """
        # if request.user == self.get_object():
        #     return render(request, f'{TEMPLATE_URL}/error_to_self.html')
        self.object_list = self.get_queryset()
        is_read_handler.send(
            sender=ReadReplyPrivateMessage,
            request=request, messages=self.object_list
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=User.objects.all()):
        return super().get_object(queryset=queryset)

    def get_queryset(self):
        user_obj = self.get_object()
        return PrivateMessage.objects.correspondence_between(self.request.user, user_obj)

    def get_slug_field(self):
        return str('username__iexact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'recipient': self.get_object()})
        return context

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
