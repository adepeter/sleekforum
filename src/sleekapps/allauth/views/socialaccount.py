from allauth.socialaccount.views import SignupView as BaseSocialAccountSignupView
from django.shortcuts import redirect
from django.urls import reverse


class SignupView(BaseSocialAccountSignupView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('sleekapps:home:home'))
        return super().get(request, *args, **kwargs)