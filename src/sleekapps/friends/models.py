from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..cores.utils.choice import Choicify

from .constants import FRIEND_REQUEST_CHOICES

friend_request_choices = Choicify(FRIEND_REQUEST_CHOICES)


class FriendRequest(models.Model):
    request_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('from'),
        on_delete=models.CASCADE,
        related_name='friend_requests_sent'
    )
    request_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('to'),
        on_delete=models.CASCADE,
        related_name='friend_requests_received'
    )
    status = models.CharField(
        verbose_name=_('request status'),
        max_length=len(friend_request_choices),
        choices=friend_request_choices.get_choices,
        default='PENDING'
    )
    date_sent = models.DateTimeField(
        verbose_name=_('date sent'),
        default=timezone.now,
        help_text=_('Date friend request was sent')
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['request_from', 'request_to'],
                name='unique_friend_request'
            )
        ]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return f'{self.request_from.get_display_name} just sent {self.request_to.get_display_name} a request'


class Friend(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='friends'
    )
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('friend\'s list'),
        through='Friendship'
    )


class Friendship(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='friendships'
    )
    friends = models.ForeignKey(
        'friends.Friend',
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(
        verbose_name=_('Date accepted'),
        auto_now_add=True,
        help_text=_('Date became friends / Date request was accepted')
    )
