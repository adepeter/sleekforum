from django.contrib import admin
from django.db.models import Count

from .models import PrivateMessage


class ReplyMessageInline(admin.StackedInline):
    model = PrivateMessage
    fk_name = 'parent'
    extra = 10
    fields = [
        'sender',
        'recipient',
        'content',
        'is_read'
    ]


@admin.register(PrivateMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'sender',
        'recipient',
        'is_read',
        'date_sent',
        'parent',
        'get_total_messages'
    ]
    list_filter = [
        'is_read'
    ]
    ordering = [
        'sender'
    ]
    date_hierarchy = 'date_sent'
    inlines = [ReplyMessageInline]

    @admin.display(description='Total Replies')
    def get_total_messages(self, message):
        return message.total_messages

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True).annotate(total_messages=Count('children'))
