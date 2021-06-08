from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from sorl.thumbnail import ImageField


class Category(models.Model):
    """Model for create categories of Ads"""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')
    
    def __str__(self):
        return 'Category: %s' % self.title
            

class Tag(models.Model):
    """Model for create Tags of Ads"""
    
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return 'Tag: %s' % self.title

from django.utils.timezone import now
from django.core.exceptions import ValidationError

def validate_birthday(birthday):
    today = now()
    if (today.year - birthday.year) < 18:
        raise ValidationError('Вам нет 18!')

class Profile(User):
    """Model of Profile (for registration new user)"""
    
    birthday = models.DateField(max_length=8, validators=[validate_birthday])
    img = ImageField(upload_to='img_html', blank=True, default='img_html/default.jpg')
    
    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk':self.pk})
    

class Seller(User):
    """Model of our Seller (users)"""
    # name = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name = "Seller")
    class Meta:
        ordering = ('first_name',)
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
    
    def __str__(self):
        return 'Seller1: %s' % self.username
    
    def nmd_of_ads():
        """Method for counting Ads for this Seller"""
    
        ads = Car.objects.count() + Stuff.objects.count() + Services.objects.count()
        return ads
    

class BaseAd(models.Model):
    """Base (Superclass) Model for different type of Ads """
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, default=None)
    
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name="продавец", related_name="%(app_label)s_%(class)s_sellers_ads", null=True)
    
    tag = models.ManyToManyField(Tag, blank=True, related_name="%(app_label)s_%(class)s_ads", related_query_name="%(app_label)s_%(class)ss",)
        
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False) 
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    class Meta:
        abstract = True


class Stuff(BaseAd):
    """Model for Ads with Stuff"""
    
    is_new = models.BooleanField(default=True)
    
    def __str__(self):
        return 'Stuff: %s' % self.title
    
    def get_absolute_url(self):
        return reverse('stuff-detail', kwargs={'pk':self.pk})


class TypeFuel(models.Model):
    """Model for creating diferent type of Fuel for Model - Car"""
    
    type_fuel = models.CharField(max_length=24, blank=True, null=True, default=None)
    def __str__(self):
        return 'TypeFuel: %s' % self.type_fuel
       
class Car(BaseAd):
    """Model for Ads with Cars"""
    
    engine_volume = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    type_fuel = models.ForeignKey(TypeFuel, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Car: %s' % self.title
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk':self.pk})
    
class Picture(models.Model):
    """Model for picture (for Car)"""
    test_field = models.CharField(max_length=100, default='test picture words')
    img = ImageField(upload_to='img_html', blank=True, default='img_html/default.jpg')
    car = models.ForeignKey(Car, blank=True, null=True, on_delete=models.CASCADE, default=None)
    
    
class Services(BaseAd):
    """Model for Ads with services"""
    
    duration = models.DateTimeField()
    def __str__(self):
        return 'Car: %s' % self.title
    
    def get_absolute_url(self):
        return reverse('services-detail', kwargs={'pk':self.pk})
    

class AdArchive(Services):
    """Proxy Model for archive and ordering Services Ads"""
        
    class Meta:
        proxy = True
        ordering = ["created_date"]

    

