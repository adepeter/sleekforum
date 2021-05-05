from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'article',
        'get_article_category',
        'is_hidden',
        'date_posted',
        'date_modified'
    ]
    list_filter = [
        'article__category',
        'is_hidden',
    ]

    @admin.display(description=_('article category'))
    def get_article_category(self, obj):
        return obj.article.category.name.title()

    __all__ = [
        'CommentAdmin'
    ]
