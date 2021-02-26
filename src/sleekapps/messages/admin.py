from django.contrib import admin

from .models import PrivateMessage


@admin.register(PrivateMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'sender',
        'recipient',
        'is_read',
        'date_sent',
        'parent'
    ]
