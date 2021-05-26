from django.urls import path
from .views import home

from django.contrib.flatpages import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
]
