from django.urls import path, include

from ..views.profile import (
    redirect_to_password_reset,
    UserProfile,
    UserProfileEdit,
    UserEmailChange,
    UserPasswordChange
)

app_name = 'profile'

urlpatterns = [
    path('', UserProfile.as_view(), name='home_profile'),
    path('edit/', UserProfileEdit.as_view(), name='profile_edit'),
    path('edit-email/', UserEmailChange.as_view(), name='profile_email_change'),
    path('password/', include([
        path('change/', UserPasswordChange.as_view(), name='profile_password_change'),
        path('force-logout/', redirect_to_password_reset, name='force_logout_to_password_reset'),
    ]))
]

urlpatterns += [
    path('<slug:username>/', include([
        path('', UserProfile.as_view(), name='user_profile'),
    ])),
]
