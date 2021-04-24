from django.contrib import admin

from ..models import ThreadView


class ThreadViewAdmin(admin.ModelAdmin):
    list_display = [
        'thread',
        'user',
        'views'
    ]


admin.site.register(ThreadView, ThreadViewAdmin)

__all__ = [
    'ThreadViewAdmin'
]
