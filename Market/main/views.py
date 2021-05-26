from django.shortcuts import render
from .models import Seller

def home(request):
    nmb_ad = Seller.nmd_of_ads()
    return render(request, 'main/index.html' , {
    'nmb_ad': nmb_ad,
    })
