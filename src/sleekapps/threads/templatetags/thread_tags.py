from django import template
from django.core.cache import cache
from ..utils.thread import get_category_threads_queryset

register = template.Library()


@register.simple_tag
def threads_in_category(category, include_self=True):
    return get_category_threads_queryset(category, include_self)


@register.simple_tag(name='threads_in_category_count')
def threads_in_category_by_count(threads, count, include_self=True):
    try:
        return threads[count]
    except IndexError:
        return threads.all()


@register.filter(name='count_reactions')
def get_reaction_count(obj, reaction):
    reaction_count = obj.get_reaction_count(reaction)
    cache.set(f'{obj.slug}_{reaction}_count', reaction_count, 10)
    return cache.get(f'{obj.slug}_{reaction}_count', None)
