import random

from django import forms
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _


class ContactUsForm(forms.Form):
    subject = forms.CharField(label=_('Heading of email'), max_length=50)
    email = forms.EmailField(label=_('Your Email Address'), widget=forms.TextInput)
    firstname = forms.CharField(label=_('Your first name'))
    lastname = forms.CharField(label=_('Your last name'))
    captcha = forms.IntegerField(
        help_text=_('Verify you are human by entering the result'),
        widget=forms.TextInput({'placeholder': _('Captcha verification')})
    )
    message = forms.CharField(
        label=_('Message content'),
        widget=forms.Textarea({'placeholder': _('Describe content of your message')}),
        help_text=_('Please ensure you send meaningful \
        message to prevent yor email from been blacklisted')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cache.get_or_set('contact_us_captcha', {
            'random_one': random.randint(10, 99),
            'random_two': random.randint(1, 10),
        }, 60)
        random_one = self.get_captcha_value('random_one')
        random_two = self.get_captcha_value('random_two')
        self.fields['captcha'].label = str(f'{random_one} \
        + {random_two}')
        self.result = sum([random_two, random_one])

    def clean_captcha(self):
        cleaned_captcha = int(self.cleaned_data['captcha'])
        if cleaned_captcha != self.result:
            cache.lock('contact_us_captcha')
            raise forms.ValidationError(_('The result is invalid'), code='invalid_result')
        return cleaned_captcha

    def get_captcha_value(self, value):
        key = cache.get('contact_us_captcha')
        return key[value]
