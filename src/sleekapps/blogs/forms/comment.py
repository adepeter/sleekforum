from django import forms
from django.utils.translation import gettext_lazy as _

from ...blogs.models import Comment


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': _('Dear %s please enter your response') % request.user.get_display_name or 'guest',
            'disabled': not request.user.is_authenticated
        })

    class Meta:
        model = Comment
        fields = [
            'content',
            'is_hidden'
        ]
