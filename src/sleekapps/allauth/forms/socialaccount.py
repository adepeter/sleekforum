from django import forms
from django.utils.translation import gettext_lazy as _
from allauth.socialaccount.forms import SignupForm as BaseSocialAccountSignupForm

from ...users.validators import validate_username


class SignupForm(BaseSocialAccountSignupForm):
    auto_id = False

    email = forms.EmailField(
        label=_('E-mail address'),
        widget=forms.EmailInput,
        disabled=True
    )
    username = forms.CharField(
        label=_('Username'),
        validators=[validate_username],
        disabled=True
    )
    accept_terms = forms.BooleanField(
        label=_('Accept registration terms'),
        initial=None,
        error_messages={
            'required': 'You need to accept registration terms to proceed'
        },
        help_text=_('Accept the following terms and conditions')
    )

    def clean_accept_terms(self):
        cleaned_accepted_terms = self.cleaned_data['accept_terms']
        if cleaned_accepted_terms is not True:
            raise forms.ValidationError(
                _('You need to accept registration terms to proceed')
            )
        return cleaned_accepted_terms

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, 'sociallogin') and 'email' in self.sociallogin.account.extra_data:
            email = self.sociallogin.account.extra_data['email']
            self.initial['email'] = email
            self.initial['username'] = email[:email.find('@')]