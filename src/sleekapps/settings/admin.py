from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Setting


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    fieldsets = [
        (_('Basic'), {'fields': ['title', 'email', 'description', 'is_under_maintenance']}),
        (_('Paginations'), {'fields': ['threads_per_page', 'posts_per_thread']}),
        (_('Registration'), {'fields': ['send_welcome_mail', 'allow_registration', 'welcome_mail']}),
        (_('Security'), {'fields': ['captcha']})
    ]
