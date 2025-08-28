from django.test import TestCase, Client

from resident.models import User


# Create your tests here.

class HouseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Hawanat",
            last_name="Olamide",
            email="hawa@gmail.com",
            password="testpassword",
            username="hawanat",
        )
        self.client = Client()

    def test_that_anonymous_user_cannot_add_house_returns_403(self):
        response = self.client.login(email="hawa@gmail.com", password="testpassword")
        'self.assertEqual(response.status_code, 403)