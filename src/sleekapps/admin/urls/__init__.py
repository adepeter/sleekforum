from django.urls import path

from ..admin import SleekForumAdmin

admin_site = SleekForumAdmin(name='admin')

app_name = 'admin'

urlpatterns = [
    path('', admin_site.urls, name='admin'),
]
