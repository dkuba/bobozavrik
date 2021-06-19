from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# from main import send_email_week

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Market.settings")
app = Celery("Market")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# @app.task
# def debug_task(ar):
#     print (ar)


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'send_email_week': {
        'task': 'main.tasks.send_email_week',
        'schedule': crontab(minute='*/1'),
        'args': ("BLa BLA BlA", ),
        # 'schedule': 5, 
    },
}

# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'send_email_week': {
#         'task': 'tasks.debug_task',
#         'schedule': crontab(minute='*/1'),
#         'args': ("BLa BLA BlA", ),
#         # 'schedule': 5, 
#     },
# }


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(minute='*/1'),
#         send_email_week(), )