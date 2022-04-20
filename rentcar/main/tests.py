from django.test import TestCase
from django.test import SimpleTestCase

from .models import CarsTable


class PageRefreshTest(SimpleTestCase):

    def test_index_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # def test_cars_page_status_code(self):
    #     response = self.client.get('/cars/')
    #     self.assertEqual(response.status_code, 200)

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
