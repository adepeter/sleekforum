from django.urls import include, path

app_name = 'sleekforum'

urlpatterns = [
    path('', include('sleekapps.home.urls', namespace='home')),
    path('notifications/', include('sleekapps.notifications.urls', namespace='notifications')),
    path('categories/', include('sleekapps.categories.urls', namespace='categories')),
    path('threads/', include('sleekapps.threads.urls', namespace='threads')),
    path('activity/', include('sleekapps.activity.urls', namespace='activity')),
    path('search/', include('sleekapps.search.urls', namespace='search')),
    path('rules/', include('sleekapps.violations.urls', namespace='violations')),
    path('pages/', include('sleekapps.pages.urls', namespace='pages')),
    path('users/', include('sleekapps.users.urls', namespace='users')),
    path('blogs/', include('sleekapps.blogs.urls', namespace='blogs')),
    path('chats/', include('sleekapps.messages.urls', namespace='messages')),
    # path('admin/', include('sleekapps.admin.urls', namespace='admin'))
]
