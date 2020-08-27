from django import template
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

register = template.Library()


@register.inclusion_tag(
    'vikinger/widgets/right_active_users.html',
    name='user_with_highest_posts')
def get_users_with_highest_post(number_of_users=10):
    query = User.objects.annotate(
            posts_count=Count('posts')
        ).exclude(
        posts_count__lt=1
    ).order_by('-posts_count')
    try:
        users = query[:number_of_users]
    except KeyError:
        users = query
    return {'users': users}
