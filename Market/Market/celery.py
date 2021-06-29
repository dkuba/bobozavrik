from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Market.settings")
app = Celery("Market")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'one-week-email': {
        'task': 'one week email',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (),
    },
}
