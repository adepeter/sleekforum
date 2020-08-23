from django import template

from ..utils.thread import get_category_threads_queryset, get_threads_in_category_by_count

register = template.Library()

@register.simple_tag
def threads_in_category(category, include_self=True):
    return get_category_threads_queryset(category, include_self)

@register.simple_tag(name='threads_in_category_count')
def get_threads_in_category_by_count(threads, count, include_self=True):
    try:
        return threads[count]
    except IndexError:
        return threads.all()
