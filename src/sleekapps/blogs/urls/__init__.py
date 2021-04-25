from django.urls import path, include

app_name = 'blogs'

urlpatterns = [
    path('<slug:username>/', include([
        path('articles/', include('sleekapps.blogs.urls.article', namespace='articles')),
        path('categories/', include('sleekapps.blogs.urls.category', namespace='categories')),
    ]))
]
