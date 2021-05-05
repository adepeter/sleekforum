from django.urls import include, path

from ..views.article import ArticlesByUserListView, UserArticlesByCategoryView

app_name = 'articles'

urlpatterns = [
    path('', ArticlesByUserListView.as_view(), name='articles'),
    path('<slug:category_slug>/', include([
        path('articles/', UserArticlesByCategoryView.as_view(), name='user_category_articles'),
    ]))
]
