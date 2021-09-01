from django.shortcuts import render
from django.urls import resolve

from ..cores.exceptions import SiteSettingsNotConfigured

from .models import Setting as Configuration


class UnderMaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        url = resolve(request.path)
        # try:
        #     settings = Configuration.load()
        #     if settings.is_under_construction and (
        #         not request.user.is_superuser or not url.route.startswith('admin')
        #     ):
        #         return render(request, 'under_maintenance.html')
        # except SiteSettingsNotConfigured:
        #     pass
        return response
