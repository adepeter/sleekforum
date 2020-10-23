from django import template

from ..models import Post

register = template.Library()


@register.simple_tag(name='posts_in_category')
def get_post_in_category_queryset(category, include_self=True):
    """Returns queryset of posts contained in a category,
    transversing through the thread field
    """
    try:
        return Post.objects.filter(
            thread__category__in=category.get_descendants(include_self=include_self)
        )
    except Post.DoesNotExist:
        return None


@register.simple_tag(name='last_post_in_category')
def get_last_post_in_category(category, include_self=True):
    try:
        return Post.objects.filter(
            thread__category__in=category.get_descendants(include_self=include_self),
            is_hidden=False
        ).latest()
    except Post.DoesNotExist:
        return None


@register.simple_tag(name='last_post')
def get_last_post_in_thread(thread):
    try:
        return Post.objects.filter(thread=thread).latest()
    except Post.DoesNotExist:
        return None


@register.simple_tag(name='global_lastpost')
def get_last_post():
    try:
        return Post.objects.latest()
    except Post.DoesNotExist:
        return None


@register.filter(name='post_count')
def count_post(user):
    return Post.objects.filter(user=user)


@register.filter
def user_last_post(user):
    earliest_post = Post.objects.filter(user=user).earliest()
    return earliest_post.created
