from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from ...activity.models import Reaction
from ...activity.viewmixins.reaction import ReactionView

from ..models import Post


class BasePostMixin:
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(thread__slug__iexact=self.kwargs['thread_slug'])

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_hidden:
            return redirect(self.request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)


class PostReactionMixin(LoginRequiredMixin, BasePostMixin, ReactionView):
    reaction_model = Reaction
    reaction_field = 'reaction'
    exclude_reactions = False