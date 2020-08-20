from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    PasswordResetForm as BasePasswordResetForm,
    SetPasswordForm as BaseSetPasswordForm
)
from django.utils.translation import gettext_lazy as _

TEMPLATE_URL = 'users/auth/password'

User = get_user_model()

class PasswordResetForm(BasePasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = _('Ensure you enter the a valid \
        email address associated with the account as a mail \
        will be sent there')
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Enter email address'),
        })

    def clean_email(self):
        cleaned_email = self.cleaned_data['email']
        get_by_email = User.objects.filter(email=cleaned_email)
        if not get_by_email.exists():
            raise forms.ValidationError(_('%s doesnt exist in our database') % cleaned_email)
        return cleaned_email

    def save(self, **kwargs):
        new_reset = super().save(**kwargs)
        subject_template_name = '%s/password_reset_subject.txt' % TEMPLATE_URL
        email_template_name = '%s/password_reset_email.html' % TEMPLATE_URL
        kwargs.update({
            'subject_template_name': subject_template_name,
            'email_template_name': email_template_name
        })
        return new_reset


class SetPasswordForm(BaseSetPasswordForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        for field in self.fields:
            password_placeholder = _('Enter new password') if field == 'new_password1' \
                else _('Repeat new password')
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                # 'placeholder': password_placeholder
            })