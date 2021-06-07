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
    fields = ["first_name", "last_name", "birthday", "email", 'img']
    template_name = 'main/profile_update.html'
    

class MyRegisterView(CreateView):
    template_name = "main/register_user.html"
    form_class = UserCreationForm
    success_url = '/'
    

class My_class:
    """MixinData class"""
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        """Add sorted_tag_list"""
        kwargs = super().get_context_data(**kwargs)
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
    
    
    def get_queryset(self):
        """filter ads by selected tag"""
        tag = self.request.GET.get('tag')
        if not tag:
            return self.model.objects.all()
        tag_obj = get_object_or_404(Tag, title=tag)
        return self.model.objects.filter(tag=tag_obj)
    
    
def home(request):
    profile = Profile.objects.get(id = 5 )
    
    nmb_ad = Seller.nmd_of_ads()
    turn_on_block = settings.MAINTENANCE_MODE
    name_seller = Seller.objects.name
    return render(request, 'main/index.html' , {
    'nmb_ad': nmb_ad,
    'turn_on_block': turn_on_block,
    'name_seller' : name_seller, 
    'profile': profile
    })

    
class CarsList(My_class, ListView ):
    model = Car
    template_name = 'main/cars_list.html'


    
class CarDetailView(DetailView):
    model = Car
    template_name = 'main/car_detail.html'


class CarAddView(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'main/car_add.html'
    
class CarEditView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'main/car_edit.html'
    

class ServicesList(My_class, ListView): 
    model = Services
    template_name = 'main/services_list.html'
    
  
    
class ServicesDetailView(DetailView):
    model = Services
    template_name = 'main/services_detail.html'
    

class StuffList(My_class, ListView):
    model = Stuff
    template_name = 'main/stuff_list.html'
    
    
class StuffDetailView(DetailView):
    model = Stuff
    template_name = 'main/stuff_detail.html'

