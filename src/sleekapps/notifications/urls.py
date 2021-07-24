from django.urls import path

from .views import NotificationListView, MarkAllAsRead

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications_list'),
    path('mark_read/', MarkAllAsRead.as_view(), name='mark_all_read'),
]
