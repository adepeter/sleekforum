from django.urls import path, include

from .views import ListPrivateMessage, ReadReplyPrivateMessage

app_name = 'messages'

urlpatterns = [
    path('', ListPrivateMessage.as_view(), name='list_private_messages'),
    path('<int:id>/<slug:username>/', include([
        path('', ReadReplyPrivateMessage.as_view(), name='read_reply_private_message'),
    ])),
]
