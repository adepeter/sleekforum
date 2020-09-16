from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.translation import gettext_lazy as _

from .models import Setting

MAX_OBJECTS = 1


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/settings/add_change_settings.html'
    list_display = ['title']
    fieldsets = [
        (_('Basic'), {'fields': ['title', 'email', 'description', 'is_under_maintenance']}),
        (_('Paginations'), {'fields': ['threads_per_page', 'posts_per_thread']}),
        (_('Registration'), {'fields': ['send_welcome_mail', 'allow_registration', 'welcome_mail']}),
        (_('Security'), {'fields': ['captcha']})
    ]

    def get_urls(self):
        urls = super().get_urls()
        my_url = [
            path('add_edit_settings/', self.add_change_settings)
        ]
        return my_url + urls

    def add_change_settings(self, request):
        if request.method == 'POST':
            return HttpResponseRedirect('/admin/settings/setting/1/change/')

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
