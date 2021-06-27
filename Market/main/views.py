from django.shortcuts import get_object_or_404, render
from .models import Tag, Seller, Profile, Services, Stuff, Car
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CarForm, CarPicturesFormset
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
)
import random
from django.core.cache import cache


class MyRegisterView(CreateView):
    """New User Register Page"""

    template_name = "main/register_user.html"
    form_class = UserCreationForm
    success_url = '/'


class MyLoginView(LoginView):
    """Login Page"""
    template_name = "main/login.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "birthday", "email", 'img']
    template_name = 'main/profile_update.html'


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


class My_CarMix:
    """MixinData class for Car (Edit and Create views)"""
    def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.seller = self.request.user
        # self.object.save()
        context = self.get_context_data(form=form)
        car_form = context['car_form']
        picture = context['picture_formset']

        if car_form.is_valid() and picture.is_valid():
            response = super().form_valid(form)
            car_form.instance = self.object
            picture.instance = self.object
            picture.save()
            car_form.save()
            return response
        else:
            return super().form_invalid(form)


# my home view
def home(request: HttpRequest) -> HttpResponse:
    profile = Profile.objects.get(id=5)
    nmb_ad = Seller.nmd_of_ads()
    turn_on_block = settings.MAINTENANCE_MODE
    name_seller = Seller.objects.name
    return render(request, 'main/index.html', {
    'nmb_ad': nmb_ad,
    'turn_on_block': turn_on_block,
    'name_seller': name_seller,
    'profile': profile
    })


class CarsList(My_class, ListView):
    """All Car (lisit)"""
    model = Car
    template_name = 'main/cars_list.html'


class CarDetailView(DetailView):
    """detail view for Car"""
    model = Car
    template_name = 'main/car_detail.html'

    """Set API cache for Car.price, update 60 sec /
    Set random coefficient for price """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_price = cache.get('object_price')
        x_car = self.object

        if random_price is None:
            random_price = random.randint(8, 12)*x_car.price*0.1
            cache.set('object_price', random_price)
            cache.touch('object_price', 60)

        context.update({
            'object':  x_car,
            'object_price': random_price,
        })

        return context


class CarAddView(PermissionRequiredMixin, My_CarMix, CreateView):
    """CarAddView"""

    permission_required = 'main.add_car'  # db - 57
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars')
    template_name = 'main/car_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['picture_formset'] = CarPicturesFormset(self.request.POST, self.request.FILES)
            context['car_form'] = CarForm(self.request.POST, self.request.FILES)
        else:
            context['picture_formset'] = CarPicturesFormset()
            context['car_form'] = CarForm()
        return context


@method_decorator(cache_page(60 * 60), name="dispatch")
class CarEditView(PermissionRequiredMixin, My_CarMix, UpdateView):
    """CarUpdateView"""
    permission_required = 'main.change_car'  # db - 58
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars')
    template_name = 'main/car_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['picture_formset'] = CarPicturesFormset(self.request.POST, self.request.FILES, instance=self.object)
            context['car_form'] = CarForm(self.request.POST, self.request.FILES, instance=self.object)
            context['picture_formset'].full_clean()
            context['car_form'].full_clean()
        else:
            context['picture_formset'] = CarPicturesFormset(instance=self.object)
            context['car_form'] = CarForm(instance=self.object)
        return context


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
