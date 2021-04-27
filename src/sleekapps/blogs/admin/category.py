from django.contrib import admin
from django.db.models import Count, Sum

from ..models import Category, Comment


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
        'num_of_articles',
        'num_of_comments',
        'description',
        'is_locked',
        'is_hidden'
    ]
    list_filter = [
        'is_hidden',
        'is_locked'
    ]
    ordering = [
        'name',
        'is_hidden',
        'is_locked',
        'owner'
    ]

    @admin.display(description='Num of articles')
    def num_of_articles(self, category):
        return category.articles_count

    @admin.display(description='Num of comments')
    def num_of_comments(self, category):
        return category.sum_comments
        # return Comment.objects.filter(article__category=category).count()

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            articles_count=Count('articles'),
            sum_comments=Count('articles__blog_comments')
        )


__all__ = [
    'CategoryAdmin'
]
