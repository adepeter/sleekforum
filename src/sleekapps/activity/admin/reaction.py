from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from ..models import Reaction


# Register your models here.

class ReactionActivityStackedInline(GenericStackedInline):
    model = Reaction
    extra = 5


@admin.register(Reaction)
class ReactionActivityAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'reaction',
        'object_id',
        'content_type',
        'content_object'
    ]


__all__ = [
    'ReactionActivityAdmin'
]
