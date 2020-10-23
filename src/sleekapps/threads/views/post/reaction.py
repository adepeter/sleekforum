from ...viewmixins.post import PostReactionMixin


class LikePost(PostReactionMixin):
    reaction = 'LIKE'


class DislikePost(PostReactionMixin):
    reaction = 'DISLIKE'


class SadPost(PostReactionMixin):
    reaction = 'SAD'


class FunnyPost(PostReactionMixin):
    reaction = 'FUNNY'


class WowPost(PostReactionMixin):
    reaction = 'WOW'


class HappyPost(PostReactionMixin):
    reaction = 'HAPPY'


class AngryPost(PostReactionMixin):
    reaction = 'ANGRY'


class LovePost(PostReactionMixin):
    reaction = 'LOVE'
