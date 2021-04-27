from django.urls import path

from ..views.category import (
    CategoryCreateView,
    CategoryListCreateView
)

app_name = 'categories'

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='categories_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
]
