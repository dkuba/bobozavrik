from django.core.mail.message import EmailMultiAlternatives
from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse
from sorl.thumbnail import ImageField
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from .tasks_models import send_feedback_email_task
from django.conf import settings
from twilio.rest import Client
import random
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    """Model for create categories of Ads"""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    def __str__(self) -> str:
        return 'Category: %s' % self.title


# Add validation birthday for Profile
def validate_birthday(birthday):
    today = now()
    if (today.year - birthday.year) < 18:
        raise ValidationError('Вам нет 18!')


class SMSLog(models.Model):
    sms_numer = models.CharField(max_length=5)
    message_sid = models.TextField()


class Profile(models.Model):
    """Model of Profile (for registration new user)"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        # null=True,
    )
    birthday = models.DateField(max_length=8, validators=[validate_birthday])
    img = ImageField(upload_to='img_html', blank=True, default='img_html/default.jpg')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        numder_phone = settings.PHONE_FROM
        client = Client(account_sid, auth_token)
        sms_numer = random.randint(1000, 9999)
        message = client.messages.create(
                                    body=sms_numer,
                                    from_=numder_phone,
                                    # to=self.phone_number
                                    to='+380959125983'
                                )
        sms_log = SMSLog()
        sms_log.sms_numer = sms_numer
        sms_log.message_sid = message.sid
        sms_log.save()
        # super(Profile, self).save(*args, **kwargs)


# Add new all User in 'common group'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        common_users, c = Group.objects.get_or_create(name='common users')
        instance.groups.add(Group.objects.get(name='common users'))


class BaseAd(models.Model):
    """Base (Superclass) Model for different type of Ads """

    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, default=None)
    publication = models.BooleanField(default=True)

    tag = ArrayField(models.CharField(max_length=200), blank=True, default = [])

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Stuff(BaseAd):
    """Model for Ads with Stuff"""

    is_new = models.BooleanField(default=True)

    def __str__(self) -> str:
        return 'Stuff: %s' % self.title

    def get_absolute_url(self):
        return reverse('stuff-detail', kwargs={'pk': self.pk})


class TypeFuel(models.Model):
    """Model for creating diferent type of Fuel for Model - Car"""

    type_fuel = models.CharField(max_length=24, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return 'TypeFuel: %s' % self.type_fuel


class Car(BaseAd):
    """Model for Ads with Cars"""

    engine_volume = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    type_fuel = models.ForeignKey(TypeFuel, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self) -> str:
        return 'Car: %s' % self.title

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})


class Picture(models.Model):
    """Model for picture (for Car)"""
    test_field = models.CharField(max_length=100, default='test picture words')
    img = ImageField(upload_to='img_html', blank=True, default='img_html/default.jpg')
    car = models.ForeignKey(Car, blank=True, null=True, on_delete=models.CASCADE, default=None)


class Services(BaseAd):
    """Model for Ads with services"""

    duration = models.DateTimeField()

    def __str__(self) -> str:
        return 'Car: %s' % self.title

    def get_absolute_url(self):
        return reverse('services-detail', kwargs={'pk': self.pk})


class AdArchive(Services):
    """Proxy Model for archive and ordering Services Ads"""

    class Meta:
        proxy = True
        ordering = ["created_date"]


class Subscriber(models.Model):
    """Model for users who subsribe to news"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return 'Subscriber: %s' % self.email


def new_user_add(sender, instance, created, **kwargs):
    """Send email for new User when registered"""
    user = instance
    if created:
        email_adress = user.email
        name = user.last_name
        data = {
            'email': email_adress,
            'name': name,
        }
        email_body = render_to_string('main/email_reg_user.html', data)
        msg = EmailMultiAlternatives(subject='реестрация аккаунта', to=[email_adress, ])
        msg.attach_alternative(email_body, 'text/html')
        msg.send()


def add_new_ad(sender, instance, created, **kwargs):
    """Send email for new User when add new Ad
    Using standart method"""
    if created:
        title = instance.title.encode('utf-8')
        for item in Subscriber.objects.all():
            email_adress = item.email
            data = {
                'email': email_adress,
                'title': title,
            }
            email_body = render_to_string('main/email_add_ad.html', data)
            msg = EmailMultiAlternatives(subject='Добавленно новое обьявление', to=[email_adress, ])
            msg.attach_alternative(email_body, 'text/html')
            msg.send()


def add_new_ad_celery(sender, instance, created, **kwargs):
    """Send email for new User when add new Ad
    Using Celery"""
    if created:
        title = instance.title
        for item in Subscriber.objects.all():
            email_adress = item.email
            data = {
                'email': email_adress,
                'title': title,
            }
            send_feedback_email_task.delay(email_adress, data)


post_save.connect(new_user_add, sender=User)
post_save.connect(add_new_ad_celery, sender=Car)
