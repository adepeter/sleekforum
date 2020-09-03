from django import template
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Count, Max
from django.utils import timezone

from ...cores.helper import get_static

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


@register.simple_tag
def user_with_highest_posts():
    return User.objects.annotate(
        max_post=Max('posts')
    ).first()

@register.filter
def country_flag_icon(user_country_alpha3code):
    country_is_not_empty = bool(user_country_alpha3code and user_country_alpha3code.strip())
    if country_is_not_empty:
        countries = cache.get('remote_countries')
        flag = [country['flag'] \
                for country in countries \
                if country['alpha3Code'] == user_country_alpha3code]
        return ''.join(flag)
    return get_static('img/flag/usa.png')

@register.filter
def age_calculator(dob):
    diff = timezone.now().date() - dob
    return diff.days // 365