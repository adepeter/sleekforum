from django.urls import include, path

app_name = 'sleekforum'

urlpatterns = [
    path('', include('sleekapps.home.urls', namespace='home')),
    path('users/', include('sleekapps.users.urls', namespace='users')),
]