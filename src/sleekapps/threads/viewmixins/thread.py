from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from ...activity.models import Reaction
from ...activity.viewmixins.reaction import ReactionView
from ..models import Thread
from .base import BooleanObjectMixin


class ThreadReactionMixin(LoginRequiredMixin, ReactionView):
    model = Thread
    reaction_model = Reaction


class ThreadSingleActionMiscView(
    BooleanObjectMixin,
    SingleObjectMixin, View
):
    redirect_to_threads = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.misc_action = self.toggle_boolean_and_save(self.object)
        return self.get_success_url()

    def get_success_url(self):
        if self.redirect_to_threads is None:
            raise ImproperlyConfigured(
                '\'redirect_to_threads\' class attr cannot be set to None. '
                'Attribute must be set to a boolean'
            )
        else:
            if self.redirect_to_threads is True:
                return redirect(self.get_redirect_url())
            return redirect(self.object.get_absolute_url())

    def get_redirect_url(self):
        return reverse('sleekforum:threads:list_threads', args=[
            str(self.kwargs['category_slug'])
        ])
