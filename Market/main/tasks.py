from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from celery.utils.log import get_task_logger

from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task( email_adress, data):
    """sends an email when feedback form is filled successfully"""
    
    msg = EmailMultiAlternatives(subject='Добавленно новое обьявление', to=[email_adress, ])
    email_body = render_to_string('main/email_add_ad.html', data)
    msg.attach_alternative(email_body, 'text/html')
    msg.send()
    
    
    
    
@task(name="send_email_week")
def send_email_week():
    """sends an email whith new ad"""
    
    
    email_adress = 'drokvadim@gmail.com'
    data = {
        'email': "email_adress",
        'title' : "title_list",
    }
    
    msg = EmailMultiAlternatives(subject='Добавленно новое обьявление', to=[email_adress, ])
    email_body = render_to_string('main/email_add_ad.html', data)
    msg.attach_alternative(email_body, 'text/html')
    msg.send()
