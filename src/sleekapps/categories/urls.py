from django.urls import include, path
from .views import (
    RootCategoryListView,
    ChildrenCategoryListView,
    ListDescendantCategoryThread,
)

app_name = 'categories'

urlpatterns = [
    path('', RootCategoryListView.as_view(), name='index'),
    path('<int:pk>/<slug:slug>/', include([
        path('', ChildrenCategoryListView.as_view(), name='subcategories'),
        path('threads/', ListDescendantCategoryThread.as_view(), name='list_threads'),
    ]))
]