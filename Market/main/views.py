from django.shortcuts import get_object_or_404, render
from .models import *
from django.conf import settings 

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView
)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "birthday", "email"]
    template_name = 'main/profile_update.html'
    

class MyRegisterView(CreateView):
    template_name = "main/register_user.html"
    form_class = UserCreationForm
    success_url = '/'
    

class My_class:
    paginate_by = 10
    
    def get_queryset(self):
        tag = self.request.GET.get('tag')
        if not tag:
            return self.model.objects.all()
        tag_obj = get_object_or_404(Tag, title=tag)
        return self.model.objects.filter(tag=tag_obj)
    
    
def home(request):
    nmb_ad = Seller.nmd_of_ads()
    turn_on_block = settings.MAINTENANCE_MODE
    name_seller = Seller.objects.name
    return render(request, 'main/index.html' , {
    'nmb_ad': nmb_ad,
    'turn_on_block': turn_on_block,
    'name_seller' : name_seller, 
    })

    
class CarsList(My_class, ListView ):
    model = Car
    template_name = 'main/cars_list.html'

    def get_context_data(self, **kwargs):
        kwargs = super(CarsList, self).get_context_data(**kwargs)
        unique_tags = set()
        tag_list = Tag.objects.all()
        model_list = self.model.objects.all()
        for tag in tag_list:
            for obj in model_list:
                if tag in obj.tag.all():
                    unique_tags.add(tag)                 
        kwargs.update({
            'unique_tags': unique_tags,
            'model': self.model,
        })
        return kwargs 
    

    
class CarDetailView(DetailView):
    model = Car
    template_name = 'main/car_detail.html'


class ServicesList(My_class, ListView): 
    model = Services
    template_name = 'main/services_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs = super(ServicesList, self).get_context_data(**kwargs)
        unique_tags = set()
        tag_list = Tag.objects.all()
        model_list = self.model.objects.all()
        for tag in tag_list:
            for obj in model_list:
                if tag in obj.tag.all():
                    unique_tags.add(tag)                 
        kwargs.update({
            'unique_tags': unique_tags,
            'model': self.model,
        })
        return kwargs 
    
    
    
    
class ServicesDetailView(DetailView):
    model = Services
    template_name = 'main/services_detail.html'
    

class StuffList(My_class, ListView):
    model = Stuff
    template_name = 'main/stuff_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs = super(StuffList, self).get_context_data(**kwargs)
        unique_tags = set()
        tag_list = Tag.objects.all()
        model_list = self.model.objects.all()
        for tag in tag_list:
            for obj in model_list:
                if tag in obj.tag.all():
                    unique_tags.add(tag)                 
        kwargs.update({
            'unique_tags': unique_tags,
            'model': self.model,
        })
        return kwargs 
    

    
class StuffDetailView(DetailView):
    model = Stuff
    template_name = 'main/stuff_detail.html'
    
       