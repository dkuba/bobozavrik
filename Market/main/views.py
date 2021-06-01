from django.shortcuts import render
from .models import Seller
from django.conf import settings 

def home(request):
    nmb_ad = Seller.nmd_of_ads()
    turn_on_block = settings.MAINTENANCE_MODE
    name_seller = Seller.objects.name
    return render(request, 'main/index.html' , {
    'nmb_ad': nmb_ad,
    'turn_on_block': turn_on_block,
    'name_seller' : name_seller 
    })
