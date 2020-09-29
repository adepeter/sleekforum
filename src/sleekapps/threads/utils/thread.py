from django.core.cache import cache

from ...cores.exceptions import CacheDoesNotExistError

from ..models import Thread


def get_category_threads_queryset(category, include_self=True):
    'Returns queryset of threads contained in a category'
    return Thread.objects.filter(
        category__in=category.get_descendants(include_self=include_self)
    )

def get_threads_in_category_by_count(category, count, include_self=True):
    try:
        return get_category_threads_queryset(category, include_self)[count]
    except IndexError:
        get_category_threads_queryset().all()

def thread_viewers(thread):
    thread_cache = cache.get('thread_views')
    viewers = thread_cache['thread_%d' % thread.id]
    return viewers