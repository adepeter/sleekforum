from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models import Thread, Post


class PostStackedInline(admin.StackedInline):
    model = Post
    extra = 5


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
        'prefix'
    ]
    inlines = [PostStackedInline]
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'thread',
        'parent',
        'content',
        'is_hidden',
        'created',
        'modified'
    ]
    search_fields = ['content', 'user', 'thread', 'parent']
    list_filter = ['user', 'thread', 'parent', 'is_hidden']
    date_hierarchy = 'created'