from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView

from ..forms.register import UserRegistrationForm

TEMPLATE_URL = 'users/auth'

User = get_user_model()


class UserRegistrationView(SuccessMessageMixin, FormView):
    form_class = UserRegistrationForm
    success_message = _('Registration was successful')
    template_name = f'{TEMPLATE_URL}/register.html'
    success_url = reverse_lazy('sleekforum:home:home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('sleekforum:home:home')
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
