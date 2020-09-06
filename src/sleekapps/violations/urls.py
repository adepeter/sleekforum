from django.urls import path

from . import views

app_name = 'violations'

urlpatterns = [
    path('', views.category, name='list_category'),
    path('<str:category>/', views.rules, name='list_rules'),
]