from django.urls import path
from django.contrib.flatpages import views

from .views import ContactUs

app_name = 'pages'

urlpatterns = [
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]

urlpatterns += [
    path('faq/', views.flatpage, {'url': '/faq/'}, name='faq'),
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about_us'),
    path('disclaimer/', views.flatpage, {'url': '/disclaimer/'}, name='disclaimer'),
    path('privacy-policy/', views.flatpage, {'url': '/privacy-policy/'}, name='privacy_policy'),
    path('terms-and-conditions/', views.flatpage, {'url': '/terms-and-conditions/'}, name='terms'),
]
