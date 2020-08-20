from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('auth/', include('sleekapps.users.urls.auth', namespace='auth')),
    path('profile/', include('sleekapps.users.urls.profile', namespace='profile')),
]