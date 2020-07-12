import os

from django.test import Client, TestCase
from django.urls import reverse

from users.models import ExpenseUser


dir_path = os.path.dirname(os.path.realpath(__file__))


class JwtExpenseUserTest(TestCase):
    fixtures = [f'{dir_path}/fixtures/created_users.json', ]

    def setUp(self) -> None:
        self.test_client = Client()
        self.jhon = ExpenseUser.objects.get(pk=1)
        self.paul = ExpenseUser.objects.get(pk=2)
        self.paul.set_password("paul1234")
        self.paul.save()
        self.jhon.set_password("abcdefg")
        self.jhon.save()

    def test_get_jwt_tokens(self):

        jhon_data = {
            "username": "jhon.lenon@test.com",
            "password": "abcdefg",
        }

        test_url = reverse('users_urls:token_obtain_pair')
        test_request = self.test_client.post(test_url, jhon_data)
        self.assertEqual(test_request.status_code, 200)
        self.assertIsNotNone(test_request.data.get('access'))
        self.assertIsNotNone(test_request.data.get('refresh'))

    def test_refresh_jwt_tokens(self):

        get_token_data = {
            "username": "jhon.lenon@test.com",
            "password": "abcdefg",
        }

        test_url = reverse('users_urls:token_obtain_pair')
        test_request = self.test_client.post(test_url, get_token_data)

        refresh_token = test_request.data.get('refresh')

        refresh_data = {
            "refresh": refresh_token,
        }

        refresh_token_url = reverse('users_urls:token_refresh')

        test_request = self.test_client.post(refresh_token_url, refresh_data)

        self.assertEqual(test_request.status_code, 200)

    def test_unauthorized_get_jwt_tokens(self):
        paul_data = {
            "username": "jhon.lenon@test.com",
            "password": "test1234",
        }

        test_url = reverse('users_urls:token_obtain_pair')
        test_request = self.test_client.post(test_url, paul_data)
        self.assertEqual(test_request.status_code, 401)
        self.assertIsNone(test_request.data.get('access'))
        self.assertIsNone(test_request.data.get('refresh'))

    def test_unauthorized_refresh_jwt_tokens(self):
        refresh_data = {
            "refresh": "test1234",
        }

        test_url = reverse('users_urls:token_refresh')
        test_request = self.test_client.post(test_url, refresh_data)
        self.assertEqual(test_request.status_code, 401)

    def test_create_user(self):
        test_create_data_user = {
            "first_name": "expensify-first",
            "last_name": "expensify-last_name",
            "email": "some.email@test.com",
            "username": "myusername",
            "password": "expenses1234"
        }

        test_url = reverse('users_urls:expense_app_user')
        test_request = self.test_client.post(test_url, test_create_data_user)
        self.assertEqual(test_request.status_code, 201)

        test_response = test_request.json().get('data')

        self.assertIsNotNone(test_response.get('token'))
        self.assertIsNotNone(test_response.get('token').get('access'))
        self.assertIsNotNone(test_response.get('token').get('refresh'))

    def test_create_already_user(self):
        test_data_user = {
            "first_name": "expensify-first",
            "last_name": "expensify-last_name",
            "email": "jhon.lenon@test.com",
            "username": "jhon.lenon@test.com",
            "password": "expenses1234"
        }

        test_url = reverse('users_urls:expense_app_user')
        test_request = self.test_client.post(test_url, test_data_user)
        self.assertEqual(test_request.status_code, 400)
