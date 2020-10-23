from django.urls import include, path
from ..views.post.post import (
    EditPost,
    DeletePost,
    ReplyPost
)
from ..views.post.report import ReportPost
from ..views.post.reaction import (
    AngryPost,
    LovePost,
    LikePost,
    DislikePost,
    SadPost,
    FunnyPost,
    HappyPost,
    WowPost
)

reactions_urlpatterns = [
    path('like/', LikePost.as_view(), name='like_post'),
    path('dislike/', DislikePost.as_view(), name='dislike_post'),
    path('happy/', HappyPost.as_view(), name='happy_post'),
    path('sad/', SadPost.as_view(), name='sad_post'),
    path('wow/', WowPost.as_view(), name='wow_post'),
    path('funny/', FunnyPost.as_view(), name='funny_post'),
    path('angry/', AngryPost.as_view(), name='angry_post'),
    path('love/', LovePost.as_view(), name='love_post'),
]

urlpatterns = [
    path('<slug:thread_slug>/<int:pk>/', include([
        path('edit/', EditPost.as_view(), name='edit_post'),
        path('delete_post/', DeletePost.as_view(), name='delete_post'),
        path('reply/', ReplyPost.as_view(), name='reply_post'),
        path('report/', ReportPost.as_view(), name='report_post'),
        path('', include(reactions_urlpatterns)),
    ])),
]
