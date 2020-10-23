from django.urls import path

from ..views.statistics import UserList

app_name = 'statistics'

urlpatterns = [
    path('', UserList.as_view(), name='users_list')
]
