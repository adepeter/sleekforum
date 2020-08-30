from django.urls import path, include

from ..views.thread.thread import ListNewestThread, ListTrendingThread

app_name = 'threads'

urlpatterns = [
    path('newest/', ListNewestThread.as_view(), name='newest_threads'),
    path('trending/', ListTrendingThread.as_view(), name='trending_threads'),
]

urlpatterns += [
    path('<slug:category_slug>/', include('sleekapps.threads.urls.thread')),
    path('posts/', include('sleekapps.threads.urls.post')),
]
