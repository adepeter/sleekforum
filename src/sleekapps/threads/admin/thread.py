from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .post import PostStackedInline
from ..models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'category',
        'starter',
        'prefix',
        'pin',
        'tags',
        'created',
        'views',
        'modified',
        'is_hidden',
        'is_locked'
    ]
    list_filter = [
        'category',
        'starter',
        'is_hidden',
        'is_locked',
        'prefix',
        'pin'
    ]
    search_fields = ['title', 'content', 'category']
    radio_fields = {
        'pin': admin.HORIZONTAL,
        'prefix': admin.HORIZONTAL,
    }
    date_hierarchy = 'created'
    save_on_top = True
    ordering = [
        'title',
        'starter',
        'pin',
        'category',
        'is_hidden',
        'is_locked',
        'created',
        'modified',
        'prefix',
        'views'
    ]
    inlines = [PostStackedInline]
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


__all__ = ['ThreadAdmin']
