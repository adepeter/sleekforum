from django.urls import path
from .views import threads

app_name = 'search'

urlpatterns = [
    path('cthreads/', threads.CategoryThreadSearch.as_view(), name='category_thread_search'),
    path('gthreads/', threads.GlobalThreadSearch.as_view(), name='global_thread_search'),
]