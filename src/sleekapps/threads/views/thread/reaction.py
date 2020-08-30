from ...viewmixins.thread import ThreadReactionMixin


class ThreadBaseReaction(ThreadReactionMixin):
    pass


class LikeThread(ThreadBaseReaction):
    reaction = 'LIKE'


class DislikeThread(ThreadBaseReaction):
    reaction = 'DISLIKE'


class SadThread(ThreadBaseReaction):
    reaction = 'SAD'


class FunnyThread(ThreadBaseReaction):
    reaction = 'FUNNY'


class WowThread(ThreadBaseReaction):
    reaction = 'WOW'


class HappyThread(ThreadBaseReaction):
    reaction = 'HAPPY'


class AngryThread(ThreadBaseReaction):
    reaction = 'ANGRY'


class LoveThread(ThreadBaseReaction):
    reaction = 'LOVE'
