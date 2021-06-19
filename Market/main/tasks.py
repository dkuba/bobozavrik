from celery.decorators import task
from django.utils.timezone import now
from .models import Car, Subscriber

from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string



@task(name="one week email")
def send_email_week():
    """sends an email whith new ad"""
    
    cars_all = Car.objects.all()
    title_list=[]
    today = now()
    for car in cars_all:
        if (today.day - car.created.day) > 7:
            new_car = car.title
            title_list.append(new_car)
            
    for item in Subscriber.objects.all():
        email_adress = item.email            
        data = {
            'email': email_adress,
            'title' : title_list,
        }
        email_body = render_to_string('main/email_add_ad.html', data)
        msg = EmailMultiAlternatives(subject='Обьявления машин', to=[email_adress, ])
        msg.attach_alternative(email_body, 'text/html')
        msg.send()
    