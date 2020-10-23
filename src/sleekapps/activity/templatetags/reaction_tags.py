from django import template
from django.contrib.auth import get_user_model
from django.core.cache import cache
from ..models import Reaction

User = get_user_model()

register = template.Library()

@register.filter
def reactions(obj, reaction):
    cached_reactions = f'{obj.slug}_{reaction}'
    if cache.get(cached_reactions) is None:
        reactions = Reaction.objects.filter_reaction_by(reaction, obj)
        cache.set(f'{obj.slug}_{reaction}', reactions)
    return cache.get(cached_reactions, None)

@register.simple_tag
def reacted_users(reaction, obj, current_user, users_to_show=6):
    reactions = obj.reactions.filter_reaction_by(reaction)
    users = User.objects.filter(activity_reactions__in=reactions)
    users = [user.username for user in users]
    if current_user in users:
        r = users.pop(users.index(current_user))
        users.insert(0, r)
        users[0] = 'You'
    if len(users) >= users_to_show:
        diff = len(users) - users_to_show
        users[users_to_show] = f' and {diff} other users'
        users = users[:users_to_show]
    return users

@register.filter
def reactions_by_user(user, reaction):
    return Reaction.objects.filter(reaction=reaction, posts__user=user, user=user)
