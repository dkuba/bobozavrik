from .models import *
def add_new_ad():
    """Send email for new User about new ad"""
    print('test_1')
    cars = Car.objects.all()
    title_list=[]
    for car in cars:
        new_car = car.title.encode('utf-8')
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
    print('test_2')
