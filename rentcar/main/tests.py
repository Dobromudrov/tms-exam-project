from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase

from django.contrib.auth import authenticate, get_user_model
from .models import CarsTable


class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test_user',
            'password': 'qwertyzxc'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class PageRefreshTest(SimpleTestCase):

    def test_index_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_conditions_page_status_code(self):
        response = self.client.get('/conditions/')
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_status_code(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

