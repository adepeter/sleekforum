from django.urls import path

from .views import ListPrivateMessage

app_name = 'messages'

urlpatterns = [
    path('', ListPrivateMessage.as_view(), name='list_private_messages')
]
