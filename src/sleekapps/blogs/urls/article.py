from django.urls import include, path

from ..views.article import (
    ArticlesByUserListView,
    ArticleByUserReadView
)

app_name = 'articles'

urlpatterns = [
    path('', ArticlesByUserListView.as_view(), name='articles'),
    path('<int:id>/<slug:slug>/', include([
        path('', ArticleByUserReadView.as_view(), name='user_read_article')
    ])),
]
