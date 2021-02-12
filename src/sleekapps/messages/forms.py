from django import forms

from .models import PrivateMessage


class BasePrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = [
            'content'
        ]


class ComposePrivateMessageForm(BasePrivateMessageForm):
    class Meta(BasePrivateMessageForm.Meta):
        fields = BasePrivateMessageForm.Meta.fields + ['recipient']


class PrivateMessageReplyForm(forms.ModelForm):
    pass
