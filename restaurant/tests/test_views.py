from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="TEST", price=80, inventory=100)

    def test_something(self):
        obj = Menu.objects.get(title='TEST')
        self.assertEqual(obj.price, 80)