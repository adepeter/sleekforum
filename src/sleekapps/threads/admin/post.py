from django.contrib import admin

from ..models import Post


class PostStackedInline(admin.StackedInline):
    model = Post
    extra = 5


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


__all__ = ['PostAdmin', 'PostStackedInline']
