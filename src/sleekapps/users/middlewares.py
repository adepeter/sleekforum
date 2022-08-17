import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.utils import timezone
from requests import ConnectTimeout

User = get_user_model()

class RedirectSocialAuthPage:
    """This middleware redirects users to sleekforum auth page instead of django_all_auth page"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse('sleekforum:users:auth:login')
        signup_url = reverse('sleekforum:users:auth:register')
        all_auth_register = reverse('account_signup')
        all_auth_login = reverse('account_login')
        current_url_path = request.path
        response = self.get_response(request)
        if current_url_path == all_auth_register:
            return redirect(signup_url)
        elif current_url_path == all_auth_login:
            return redirect(login_url)
        else:
            return response


class OnlineStatusMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        now = timezone.now()
        if request.user.is_authenticated:
            cache.set(f'seen_{current_user.username}', now,
                      settings.USER_LASTSEEN_TIMEOUT)
        response = self.get_response(request)
        get_last_seen = cache.get(f'seen_{current_user.username}', now)
        diff = now - get_last_seen
        if diff.seconds < 5:
            try:
                user = User.objects.get(username=current_user.username)
                user.last_seen = now
                user.save(update_fields=['last_seen'])
            except User.DoesNotExist:
                pass

        return response


class FetchCountryFromAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if cache.get('remote_countries') is None:
            api_url = 'https://countrylayer.com/rest/v2/all'
            result = []
            try:
                api_response = requests.get(api_url, params={'access_key': settings.COUNTRYLAYER_X_API_KEY})
                if api_response.status_code == 200:
                    result = api_response.json()
            except ConnectTimeout:
                pass
            print('Result is: ', result)
            cache.set('remote_countries', result, timeout=None)
        return self.get_response(request)
