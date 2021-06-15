# from bobozavrik.Market.main import scheduler
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from . import scheduler
        scheduler.start()