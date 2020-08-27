from ....activity.models import Reaction
from ...viewmixins.thread import ThreadReactionMixin
from ...models import Thread


class LikeThread(ThreadReactionMixin):
    model = Thread
    reaction_model = Reaction
    reaction = 'LIKE'


class DislikeThread(ThreadReactionMixin):
    model = Thread
    reaction_model = Reaction
    reaction = 'DISLIKE'


class SadThread(ThreadReactionMixin):
    model = Thread
    reaction_model = Reaction
    reaction = 'SAD'


class FunnyThread(ThreadReactionMixin):
    model = Thread
    reaction_model = Reaction
    reaction = 'FUNNY'


class WowThread(ThreadReactionMixin):
    model = Thread
    reaction_model = Reaction
    reaction = 'WOW'
