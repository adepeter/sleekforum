from django.urls import path, include

from ..views.thread.thread import (
    ListThread,
    CreateThread,
    ReadThread,
    EditThread,
    DeleteThread
)
from ..views.thread.hide_unhide import HideUnhideThread
from ..views.thread.lock_unlock import LockUnlockThread
from ..views.thread.reaction import (
    DislikeThread,
    LikeThread,
    FunnyThread,
    SadThread,
    WowThread,
    HappyThread,
    LoveThread,
    AngryThread
)
from ..views.thread.report import ReportThread
from ..views.thread.thread_misc import (
    ShareThread,
)

urlpatterns = [
    path('<int:category_id>/', include([
        path('', ListThread.as_view(), name='list_threads'),
        path('create/', CreateThread.as_view(), name='create_thread'),
    ])),
]

urlpatterns += [
    path('<int:pk>/<slug:slug>/', include([
        path('', ReadThread.as_view(), name='read_thread'),
        path('edit/', EditThread.as_view(), name='edit_thread'),
        path('delete/', DeleteThread.as_view(), name='delete_thread'),
        path('share/', ShareThread.as_view(), name='share_thread'),
        path('report/', ReportThread.as_view(), name='report_thread'),
        path('hide-unhide/', HideUnhideThread.as_view(), name='toggle_hide_thread'),
        path('lock-unlock/', LockUnlockThread.as_view(), name='toggle_lock_thread'),
        path('like/', LikeThread.as_view(), name='like_thread'),
        path('dislike/', DislikeThread.as_view(), name='dislike_thread'),
        path('wow/', WowThread.as_view(), name='wow_thread'),
        path('funny/', FunnyThread.as_view(), name='funny_thread'),
        path('sad/', SadThread.as_view(), name='sad_thread'),
        path('angry/', AngryThread.as_view(), name='angry_thread'),
        path('love/', LoveThread.as_view(), name='love_thread'),
        path('happy/', HappyThread.as_view(), name='happy_thread'),
    ])),
]
