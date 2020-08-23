from django import template

from ..models import Post

register = template.Library()

@register.simple_tag(name='posts_in_category')
def get_post_in_category_queryset(category, include_self=True):
    """Returns queryset of posts contained in a category,
    transversing through the thread field
    """
    return Post.objects.filter(
        thread__category__in=category.get_descendants(include_self=include_self)
    )


@register.simple_tag(name='last_post')
def get_last_post_in_thread(thread):
    try:
        return Post.objects.filter(thread=thread).latest()
    except Post.DoesNotExist:
        return None

@register.filter(name='post_count')
def count_post(user):
    return Post.objects.filter(user=user)