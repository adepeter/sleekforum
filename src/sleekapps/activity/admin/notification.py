from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from ..models import Notification


class NotificationActivityStackedInline(GenericStackedInline):
    model = Notification
    extra = 5


@admin.register(Notification)
class NotificationActivityAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'object_id',
        'content_type',
        'content_object'
    ]
    inlines = [
        NotificationActivityStackedInline,
    ]


__all__ = [
    'NotificationActivityAdmin'
]
