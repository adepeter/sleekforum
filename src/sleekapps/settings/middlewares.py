from django.shortcuts import render
from django.urls import resolve, reverse
from .models import Setting as Configuration


class UnderMaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        settings = Configuration.load()
        if settings.is_under_maintenance:
            if not request.user.is_superuser or not self.resolve_path('admin:index'):
                return render(request, 'under_maintenance.html')
        response = self.get_response(request)
        return response

    def resolve_path(self, url_path):
        return resolve(reverse(url_path))
