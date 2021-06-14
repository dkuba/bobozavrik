from django.urls import path
from .views import * 

from django.contrib.flatpages import views

urlpatterns = [
    path('register/', MyRegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    
    path('', home, name='home'),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
    
    path('cars/add/', car_add, name='cars-add'),
    path('cars/<int:pk>/edit/', manage_picture, name='cars-update'),
    
    path('accounts/profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'), 
    
    path('cars/', CarsList.as_view(), name='cars'),    
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    
    path('services/', ServicesList.as_view(), name='services'),
    path('services/<int:pk>/', ServicesDetailView.as_view(), name='services-detail'),
    
    path('stuff/', StuffList.as_view(), name='stuff'),
    path('stuff/<int:pk>/', StuffDetailView.as_view(), name='stuff-detail'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)