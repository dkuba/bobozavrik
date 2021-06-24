from django.urls import include, path
from .views import * 
from django.contrib.flatpages import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from allauth.account.views import confirm_email as allauthemailconfirmation
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page


urlpatterns = [    
    path('register/', MyRegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
    
    path('cars/add/', CarAddView.as_view(), name='cars-add'),
    path('cars/<int:pk>/edit/', CarEditView.as_view(), name='cars-update'),
    
    path('accounts/profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'), 
    
    path('cars/', CarsList.as_view(), name='cars'),    
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    
    path('services/', ServicesList.as_view(), name='services'),
    path('services/<int:pk>/', ServicesDetailView.as_view(), name='services-detail'),
    
    path('stuff/', StuffList.as_view(), name='stuff'),
    path('stuff/<int:pk>/', StuffDetailView.as_view(), name='stuff-detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)