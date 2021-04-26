from django.contrib import admin
from django.db.models import Count

from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = [
        'icon',
        'name'
    ]
    list_display = [
        'icon',
        'name',
        'owner',
        'slug',
        'description',
        'is_locked',
        'is_hidden'
    ]
    list_filter = [
        'is_hidden',
        'is_locked'
    ]

    @admin.display(description='')
    def get_articles(self, category):
        return category.articles_count

    def get_queryset(self, request):
        return super().get_queryset().annotate(
            articles_count=Count('article'),
            comments_count=Count('comments')
        )


__all__ = [
    'CategoryAdmin'
]
