from django.urls import path, include

from ..views.category import (
    CategoryEditDeleteView,
    CategoryListCreateView
)

app_name = 'categories'

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='categories_list_create'),
    path('<slug:slug>/', include([
        path('edit/', CategoryEditDeleteView.as_view(), name='category_edit_delete'),
    ]))
]
