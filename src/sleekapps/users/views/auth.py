from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)

from ..forms.auth import AuthenticationForm

TEMPLATE_URL = 'users/auth'


class LoginView(BaseLoginView):
    template_name = f'{TEMPLATE_URL}/login.html'
    form_class = AuthenticationForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(self.request, f'{TEMPLATE_URL}/session_active.html')
        return super().get(*args, **kwargs)


class LogoutView(BaseLogoutView):
    pass
