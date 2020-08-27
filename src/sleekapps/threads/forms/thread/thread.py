from django import forms
from django.utils.translation import gettext_lazy as _

from ...models import Thread


class BaseThreadForm(forms.ModelForm):
    error_messages = {
        'title': {
            'required': _('This field cannot be left empty')
        },

    }

    class Meta:
        model = Thread
        fields = ['title', 'prefix', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter thread title')
            }),
            'content': forms.Textarea(attrs={
                'rows': 15,
                'placeholder': _('Let\'s get started'),
            })
        }


class ThreadCreationForm(BaseThreadForm):
    class Meta(BaseThreadForm.Meta):
        help_texts = {
            'title': _('Describe your topic well, while keeping \
            the subject as short as possible.'),
        }


class AdminThreadCreationForm(ThreadCreationForm):
    class Meta(ThreadCreationForm.Meta):
        fields = ThreadCreationForm.Meta.fields + ['category']


class ThreadEditForm(BaseThreadForm):

    class Meta(BaseThreadForm.Meta):
        fields = BaseThreadForm.Meta.fields + ['tags']

    def save(self, commit=True):
        new_thread = super().save(commit=False)
        if commit:
            new_thread.save()
        return new_thread


class AdminThreadEditForm(ThreadEditForm):
    class Meta(ThreadEditForm.Meta):
        fields = ThreadEditForm.Meta.fields + ['category']
