from django.urls import include, path
from ..views.profile import (
UserContentCategoryList,
    UserProfile,
    UserProfileStatistics,
    ListUserThreads
)

app_name = 'users'

urlpatterns = [
    path('auth/', include('sleekapps.users.urls.auth', namespace='auth')),
    path('profile/', include('sleekapps.users.urls.profile', namespace='profile')),
    path('statistics/', include('sleekapps.users.urls.statistics', namespace='statistics')),
]

urlpatterns += [
    path('<username>/', include([
        path('', UserProfile.as_view(), name='kwarg_home_profile'),
        path('categories/', UserContentCategoryList.as_view(), name='user_categories_list'),
        path('threads/', ListUserThreads.as_view(), name='user_threads_list'),
        path('statistics/', UserProfileStatistics.as_view(), name='user_profile_statistics'),
    ])),
]
