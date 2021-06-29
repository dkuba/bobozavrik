from django.test import TestCase

from main.models import Car
from django.urls import reverse


class CarListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 cars for pagination tests
        number_of_cars = 13
        for car_num in range(number_of_cars):
            Car.objects.create(title='Christian %s' % car_num, description = 'Surname %s' % car_num, price = 1)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cars/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cars'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cars'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/cars_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cars'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['object_list']) == 10)

    def test_lists_all_authors(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('cars')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['object_list']) == 3)