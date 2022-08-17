from django.urls import path, include

from .views.socialaccount import SignupView

urlpatterns = [
    path('social/', include([
        path('signup/', SignupView.as_view(), name='socialaccount_signup'),
        path('', include('allauth.socialaccount.urls')),
    ])),
    path('', include('allauth.urls')),
]
