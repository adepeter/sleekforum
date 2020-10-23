from django.urls import path, include

from ..views.thread.thread import (
    create_quick_thread,
    ListNewestThread,
    ListTrendingThread
)

app_name = 'threads'

urlpatterns = [
    path('create-quick-post/', create_quick_thread, name='create_quick_thread'),
    path('newest/', ListNewestThread.as_view(), name='newest_threads'),
    path('trending/', ListTrendingThread.as_view(), name='trending_threads'),
]

urlpatterns += [
    path('<slug:category_slug>/', include('sleekapps.threads.urls.thread')),
    path('posts/', include('sleekapps.threads.urls.post')),
]
