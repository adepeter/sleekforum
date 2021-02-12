from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'sender',
        'recipient',
        'is_read',
        'date_sent',
        'parent'
    ]
