from django.contrib import admin
from django.db.models import Count
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
        'date_modified',
        'get_comments_count'
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

    @admin.display(description=_('Num of comments'))
    def get_comments_count(self, obj):
        return obj.num_of_comments

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(num_of_comments=Count('blog_comments'))


__all__ = [
    'ArticleAdmin'
]
