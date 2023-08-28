from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='username',
            password='password'
        )
        self.test = Menu.objects.create(title="TEST", price=80, inventory=100)
        self.test2 = Menu.objects.create(title="TEST2", price=80, inventory=100)

    def login(self) -> None:
        self.client.login(username='testuser', password='testpassword')

    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('items'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        serializer = menuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)

