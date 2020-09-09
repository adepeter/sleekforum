from django.urls import path
from .views import threads

app_name = 'search'

urlpatterns = [
    path('gthreads/', threads.GlobalThreadSearch.as_view(), name='global_thread_search'),
]