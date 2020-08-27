from django import forms
from django.utils.translation import gettext_lazy as _

from ...models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        user = self.request.user
        super().__init__(*args, **kwargs)
        login_placeholder = _(f'Hi {user.username} share your post here let\'s get started')
        guest_placeholder = _('Dear guest, login to post a reply')
        self.fields['content'].widget.attrs.update({
            'id': 'form-post-text',
            'rows': '5',
            'placeholder': login_placeholder if user.is_authenticated else guest_placeholder,
            'disabled': True if not user.is_authenticated else False
        })

    def is_valid(self):
        invalid_form = super().is_valid()
        for field in (self.fields if '__all__' in self.errors else self.errors):
            self.fields[field].widget.attrs.update({'class': 'form-control is-invalid'})
        return invalid_form


class PostForm(BasePostForm):
    pass


class PostEditForm(BasePostForm):
    pass
