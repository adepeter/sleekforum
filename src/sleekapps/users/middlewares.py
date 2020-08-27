import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils import timezone

User = get_user_model()


class OnlineStatusMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        if request.user.is_authenticated:
            now = timezone.now()
            cache.set(f'seen_{current_user.username}', now,
                      settings.USER_LASTSEEN_TIMEOUT)
        response = self.get_response(request)
        return response


class FetchCountryFromAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_url = 'https://restcountries.eu/rest/v2/all'
        api_response = requests.get(api_url)
        if api_response.status_code == 200:
            result = api_response.json()
            cache.set('remote_countries', result, timeout=None)
        response = self.get_response(request)
        return response
