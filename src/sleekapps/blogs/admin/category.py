from django.contrib import admin

from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'description',
        'is_locked',
        'is_hidden'
    ]


__all__ = [
    'CategoryAdmin'
]
