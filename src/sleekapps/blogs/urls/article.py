from django.urls import include, path

from ..views.article import ArticlesByUserListView

app_name = 'articles'

urlpatterns = [
    path('', ArticlesByUserListView.as_view(), name='articles'),
]
