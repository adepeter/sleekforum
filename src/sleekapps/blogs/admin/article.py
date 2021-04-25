from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug', 'completion_status', 'date_created', 'date_modified'
    ]
    list_display = [
        'author',
        'category',
        'title',
        'completion_status',
        'slug',
        'tags',
        'cover',
        'content',
        'is_locked',
        'is_hidden',
        'date_created',
        'date_modified'
    ]
    search_fields = [
        'title',
        'slug',
        'content',
        'author__username',
        'author__email'
    ]
    list_filter = [
        'is_hidden',
        'is_locked'
    ]
    list_display_links = [
        'title'
    ]
    fieldsets = [
        (_('Basics'), {
            'description': 'Compulsory article data',
            'fields': (['author', 'title', 'category', 'slug', 'tags', 'completion_status']),
        }),
        (_('Cover'), {
            'description': 'Cover photo for blog',
            'fields': ['cover']
        }),
        (_('Privacy'), {
            'description': 'Visibility of article',
            'fields': ['is_hidden', 'is_locked']
        }),
        (_('Important dates'), {
            'description': 'Time stamp records',
            'fields': ['date_created', 'date_modified']
        })
    ]
    date_hierarchy = 'date_created'


__all__ = [
    'ArticleAdmin'
]
