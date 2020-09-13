from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Setting


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    fieldsets = [
        (_('Basic'), {'fields': ['title', 'description']}),
        (_('Paginations'), {'fields': ['threads_per_page', 'posts_per_thread']}),
    ]
