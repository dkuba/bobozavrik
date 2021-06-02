from django.shortcuts import render
from .models import *
from django.conf import settings 
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    DetailView,
)


def home(request):
    nmb_ad = Seller.nmd_of_ads()
    turn_on_block = settings.MAINTENANCE_MODE
    name_seller = Seller.objects.name
    return render(request, 'main/index.html' , {
    'nmb_ad': nmb_ad,
    'turn_on_block': turn_on_block,
    'name_seller' : name_seller, 
    })
    
    
class CarsList(ListView):
    queryset = Car.objects.all()
    template_name = 'main/cars_list.html'
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'main/car_detail.html'


class ServicesList(ListView):
    queryset = Services.objects.all()
    template_name = 'main/services_list.html'
    
class ServicesDetailView(DetailView):
    model = Services
    template_name = 'main/services_detail.html'
    

class StuffList(ListView):
    queryset = Stuff.objects.all()
    template_name = 'main/stuff_list.html'
    
class StuffDetailView(DetailView):
    model = Stuff
    template_name = 'main/stuff_detail.html'