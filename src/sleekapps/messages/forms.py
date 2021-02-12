from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import PrivateMessage

User = get_user_model()


class BasePrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = [
            'content'
        ]


class ComposePrivateMessageForm(BasePrivateMessageForm):
    field_order = [
        'recipient',
    ]

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super().__init__(*args, **kwargs)
        # self.fields['recipient'].queryset = User.objects.exclude(id=current_user.id)

    class Meta(BasePrivateMessageForm.Meta):
        fields = BasePrivateMessageForm.Meta.fields + ['recipient']


class PrivateMessageReplyForm(BasePrivateMessageForm):

    def __init__(self, sender, recipient, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': _('Write message to %(recipient)s' % {'recipient': recipient.get_display_name}),
            'disabled': recipient == sender
        })

    class Meta(BasePrivateMessageForm.Meta):
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': _('Send a message'),
                'disabled': True
            })
        }
