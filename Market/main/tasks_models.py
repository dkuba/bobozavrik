from celery.decorators import task
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string

@task(name="send_feedback_email_task")
def send_feedback_email_task( email_adress, data):
    """sends an email when feedback form is filled successfully"""
    
    msg = EmailMultiAlternatives(subject='Добавленно новое обьявление', to=[email_adress, ])
    email_body = render_to_string('main/email_add_ad.html', data)
    msg.attach_alternative(email_body, 'text/html')
    msg.send()