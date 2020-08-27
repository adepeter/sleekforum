from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ..services.location import fetch_country
from ..validators import validate_phone_number, validate_unique_user

User = get_user_model()

countries = fetch_country()

class UserEmailEditForm(forms.ModelForm):
    """User email change with password for confirmation"""
    new_email = forms.EmailField(
        label=_('New e-mail'),
        widget=forms.TextInput
    )
    password = forms.CharField(
        label=_('Account password'),
        widget=forms.PasswordInput,
        help_text=_('Provide your account password'),
        strip=False
    )

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.TextInput,
        }

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True

    def clean_new_email(self):
        cleaned_new_email = self.cleaned_data['new_email']
        validate_unique_user(
            error_message=_('E-mail is already taken'),
            email=cleaned_new_email
        )
        return cleaned_new_email

    def clean_password(self):
        cleaned_password = self.cleaned_data['password']
        if not self.user.check_password(cleaned_password):
            raise forms.ValidationError(_('Incorrect password input'))
        return cleaned_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['new_email']
        if commit:
            user.save()
        return user

class UserSearchForm(forms.Form):
    keyword = forms.CharField(
        label=_('E-mail or username'),
        help_text=_('Kindly enter \
        the e-mail, username or profile display name of user')
    )


class UserProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        country_choices = [
            (country['alpha3Code'], _(country['name'])) for country in countries
        ]
        self.fields['dob'] = forms.DateField(
            help_text=_('Birth date in yyyy-mm-dd format'),
            input_formats=['%Y-%m-%d'],
            widget=forms.DateInput(attrs={
                'data-toggle': 'datepicker'
            })
        )
        self.fields['country'] = forms.ChoiceField(choices=country_choices)
        self.fields['phone_number'].validators.append(validate_phone_number)
        self.fields['whatsapp'].validators.append(validate_phone_number)



    class Meta:
        model = User
        widgets = {
            'hobbies': forms.Textarea
        }
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'sex',
            'dob',
            'signature',
            'hobbies',
            'about',
            'phone_number',
            'address',
            'state',
            'country',
            'facebook',
            'twitter',
            'website',
            'repo',
            'whatsapp',
        ]