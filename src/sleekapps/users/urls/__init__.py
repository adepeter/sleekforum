from django.urls import include, path
from ..views.profile import UserProfile, UserProfileStatistics

app_name = 'users'

urlpatterns = [
    path('auth/', include('sleekapps.users.urls.auth', namespace='auth')),
    path('profile/', include('sleekapps.users.urls.profile', namespace='profile')),
    path('statistics/', include('sleekapps.users.urls.statistics', namespace='statistics')),
]

urlpatterns += [
    path('<username>/', include([
        path('', UserProfile.as_view(), name='kwarg_home_profile'),
        path('statistics/', UserProfileStatistics.as_view(), name='user_profile_statistics'),
    ])),
]