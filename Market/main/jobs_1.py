from .models import Car, Subscriber, EmailMultiAlternatives, render_to_string
from django.utils.timezone import now


def add_new_ad():
    """Send email for new User about new ad for last 7 days"""

    cars = Car.objects.all()
    title_list = []
    today = now()
    for car in cars:
        if (today.day - car.created.day) > 7:
            new_car = car.title.encode('utf-8')
            title_list.append(new_car)
    for item in Subscriber.objects.all():
        email_adress = item.email
        data = {
            'email': email_adress,
            'title': title_list,
        }
        email_body = render_to_string('main/email_add_ad.html', data)
        msg = EmailMultiAlternatives(subject='Обьявления машин', to=[email_adress, ])
        msg.attach_alternative(email_body, 'text/html')
        msg.send()
