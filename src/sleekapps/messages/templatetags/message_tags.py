from django import template
from django.urls import reverse

from ..models import PrivateMessage

register = template.Library()


@register.simple_tag
def last_message(parent_message):
    return PrivateMessage.objects.filter(parent=parent_message).last()


@register.filter(name='redirect_url')
def get_absolute_url(request, message):
    redirect_url = message.get_absolute_url()
    if message.recipient == request.user:
        kwargs = {
            'id': message.sender.id,
            'username': message.sender.username
        }
        redirect_url = reverse('sleekforum:messages:read_reply_private_message', kwargs=kwargs)
    return redirect_url
