from django import forms
from django.utils.translation import gettext_lazy as _


class ContactUsForm(forms.Form):
    sender_email = forms.EmailField(label=_('Your Email Address'))
    sender_firstname = forms.CharField(label=_('Your first name'))
    sender_lastname = forms.CharField(label=_('Your last name'))
    content = forms.CharField(label=_('Message content'), widget=forms.Textarea)

    def send_message(self):
        pass
