from django.urls import path
from .views.base import Homepage

app_name = 'home'

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
]