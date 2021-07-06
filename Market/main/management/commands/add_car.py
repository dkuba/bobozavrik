from django.core.management.base import BaseCommand
from main.models import Car
import factory


class CarFactory(factory.django.DjangoModelFactory):
    # use factory for generation Car models
    class Meta:
        model = Car

    title = factory.Iterator(["France", "Italy", "Spain"])
    description = factory.Iterator(['fr', 'it', 'es'])


class Command(BaseCommand):
    """ 
    add command for manage.py, generation Car models for db
    python manage.py add_car --cars (default 3 or your number) 
    """
    
    def add_arguments(self, parser):
        # number of car
        parser.add_argument('--cars',
            default=3,
            type=int)

    def handle(self, *args, **options):
        # created cars
        for _ in range(options['cars']):
            CarFactory.create()
