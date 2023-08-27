from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')

    def test_get_all(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chips", price=40, inventory=50)
        items = Menu.objects.all()
        self.assertEqual(items, 'IceCream : 80, Chips : 40')