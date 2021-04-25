from django.urls import path

from ..views.category import CategoryListView

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories_list')
]
