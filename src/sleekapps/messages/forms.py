from django import forms

from .models import Message


class BasePrivateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'content'
        ]


class ComposePrivateMessageForm(BasePrivateMessageForm):
    class Meta(BasePrivateMessageForm.Meta):
        fields = BasePrivateMessageForm.Meta.fields + ['recipient']


class PrivateMessageReplyForm(forms.ModelForm):
    pass
