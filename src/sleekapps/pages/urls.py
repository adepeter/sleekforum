from django.urls import path
from django.contrib.flatpages import views

app_name = 'pages'

urlpatterns = [
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about_us'),
    path('privacy-policy/', views.flatpage, {'url': '/privacy-policy/'}, name='privacy_policy'),
    path('terms-and-conditions/', views.flatpage, {'url': '/terms-and-conditions/'}, name='terms'),
]
