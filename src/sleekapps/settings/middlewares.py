from django.urls import resolve, reverse
from .models import Setting as Configuration



class UnderMaintainanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # settings = Configuration.objects.get()
        print(resolve(reverse('sleekforum:home:home')))
        # if settings.is_under_maintenance:
        #     if self.resolve_path('')

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def resolve_path(self, url_path):
        return resolve(url_path)
