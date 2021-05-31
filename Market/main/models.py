from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Model for create categories of Ads"""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    def __str__(self):
        return 'Category: %s' % self.title
    
    
class Ad(models.Model):
    """Model for create Ads"""
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=True, null=True)
    
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, default=None)
    
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False) 
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    def __str__(self):
        return 'Ad: %s' % self.title


class AdArchive(Ad):
    """Proxy Model for archive and ordering Ads"""
        
    class Meta:
        proxy = True
        ordering = ["created_date"]
        

class Tag(models.Model):
    """Model for create Tags of Ads"""
    
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return 'Tag: %s' % self.title


class Seller(User):
    """Model of our Seller (users)"""
    name = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name = "Seller")
    
    def __str__(self):
        return 'Seller: %s' % self.title
    
    def nmd_of_ads():
        """Method for counting Ads for this Seller"""
        
        nmb_ad = Ad.objects.count()
        return nmb_ad
    

class BaseAd(models.Model):
    """Base (Superclass) Model for different type of Ads """
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Stuff(BaseAd):
    """Model for Ads with Stuff"""
    
    is_new = models.BooleanField(default=True)
    
    def __str__(self):
        return 'Stuff: %s' % self.title


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
    
    
class Services(BaseAd):
    """Model for Ads with services"""
    
    duration = models.DateTimeField()
    def __str__(self):
        return 'Car: %s' % self.title
    
    

    

