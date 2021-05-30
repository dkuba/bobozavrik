from django.db import models
from django.contrib.auth.models import User

# from django.utils.text import slugify
# import random
# import string

# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    def __str__(self):
        return 'Category: %s' % self.title
    
    # def unique_slug_generator(instance, new_slug=None):
    #     """
    #     This is for a Django project and it assumes your instance 
    #     has a model with a slug field and a title character (char) field.
    #     """
    #     if new_slug is not None:
    #         slug = new_slug
    #     else:
    #         slug = slugify(instance.title)

    #     Klass = instance.__class__
    #     qs_exists = Klass.objects.filter(slug=slug).exists()
    #     if qs_exists:
    #         new_slug = "{slug}-{randstr}".format(
    #                     slug=slug,
    #                     randstr=random_string_generator(size=4)
    #                 )
    #         return unique_slug_generator(instance, new_slug=new_slug)
    #     return slug

    
class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, default=None)
    
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False) 
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    def __str__(self):
        return 'Ad: %s' % self.title


class AdArchive(Ad):
    
    class Meta:
        proxy = True
        ordering = ["created_date"]
        

class Tag(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return 'Tag: %s' % self.title


class Seller(User):
    name = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name = "Seller")
    
    def __str__(self):
        return 'Seller: %s' % self.title
    
    def nmd_of_ads():
        nmb_ad = Ad.objects.count()
        return nmb_ad
    

class BaseAd(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Stuff(BaseAd):
    is_new = models.BooleanField(default=True)
    
    def __str__(self):
        return 'Stuff: %s' % self.title


class TypeFuel(models.Model):
    type_fuel = models.CharField(max_length=24, blank=True, null=True, default=None)
    def __str__(self):
        return 'TypeFuel: %s' % self.type_fuel
       
class Car(BaseAd):
    engine_volume = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    type_fuel = models.ForeignKey(TypeFuel, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Car: %s' % self.title
    
    
class Services(BaseAd):
    duration = models.DateTimeField()
    def __str__(self):
        return 'Car: %s' % self.title
    
    

    

