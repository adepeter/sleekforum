from django.urls import path

from . import views

urlpatterns = [
    path('', views.visits, name='visits'),
]
