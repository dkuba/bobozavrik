from django.test import TestCase

from django.contrib.auth import get_user_model
from main.models import Ad, Category

User = get_user_model()


class AdTestCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')

    def test_add_Ad(self):
        self.categoryT = Category.objects.create(title='Категория1', slug='Cat1')
        self.ad = Ad.objects.create(title='create new Ad', description='tests.py "create"', category=self.categoryT)
        self.all_Ad = Ad.objects.all()
        self.g = Ad.objects.get(title='create new Ad')
        self.test_filter = Ad.objects.filter(category='1')
        self.b = Ad(title='New Ad', description='tests.py "save" ')
        self.b.save()
