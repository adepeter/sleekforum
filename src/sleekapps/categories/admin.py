from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from django.utils.translation import (
    ngettext,
    gettext_lazy as _
)

from mptt.admin import DraggableMPTTAdmin

from .models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    actions = ['lock_section', 'unlock_section']
    mptt_indent_field = 'name'
    list_display_links = ['indented_title']
    readonly_fields = [
        'image_preview'
    ]
    list_display = [
        'tree_actions',
        'indented_title',
        'name',
        'is_lock',
        'parent',
        'thread_count'
    ]
    search_fields = ['name', 'description', 'parent']
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_filter = [
        'parent',
        'is_lock',
    ]
    fieldsets = [
        (_('Parent'), {
            'fields': ['parent']
        }),
        (_('Category Icon'), {
            'fields': ['image', 'image_preview']
        }),
        (_('Basic Fields'), {
            'fields': ['name', 'slug', 'is_lock', 'description']
        }),
    ]
    save_on_top = True
    mptt_level_indent = 20

    def lock_section(self, request, queryset):
        queryset.update(is_lock=True)
        message = ngettext(
            _('Category successfully locked'),
            _('Categories successfully locked'),
            queryset.count()
        )
        messages.success(request, '%(message)s' % {'message': message})

    lock_section.short_description = _('Lock selected')

    def image_preview(self, obj):
        image_url = obj.image.url
        print(image_url)
        return mark_safe('<img src="%s" height="64" width="64" />' % image_url)

    image_preview.short_description = _('Folder image')

    def thread_count(self, obj):
        if obj.threads.exists():
            return obj.threads.count()
        return 0

    thread_count.short_description = _('Thread counts')

    def unlock_section(self, request, queryset):
        queryset.update(is_lock=False)
        message = ngettext(
            _('Category successfully unlocked'),
            _('Categories successfully unlocked'),
            queryset.count()
        )
        messages.success(request, '%(message)s' % {'message': message})

    unlock_section.short_description = _('Unlock selected')
