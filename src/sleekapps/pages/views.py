from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import cache
from django.core.mail import send_mail
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import ContactUsForm


class ContactUs(SuccessMessageMixin, FormView):
    template_name = 'flatpages/contact_us.html'
    form_class = ContactUsForm
    success_message = _('Message was successfully sent, please await response soon')
    success_url = reverse_lazy('sleekforum:pages:contact_us')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        send_mail(
            cleaned_data['subject'],
            cleaned_data['message'],
            cleaned_data['email'],
            ['adepeter26@gmail.com']
        )
        cache.delete('contact_us_captcha')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('There seem to be an issue with submitted data'))
        return super().form_invalid(form)