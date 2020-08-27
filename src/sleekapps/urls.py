from django.urls import include, path

app_name = 'sleekforum'

urlpatterns = [
    path('', include('sleekapps.home.urls', namespace='home')),
    path('categories/', include('sleekapps.categories.urls', namespace='categories')),
    path('threads/', include('sleekapps.threads.urls', namespace='threads')),
    path('search/', include('sleekapps.search.urls', namespace='search')),
    path('users/', include('sleekapps.users.urls', namespace='users')),
]