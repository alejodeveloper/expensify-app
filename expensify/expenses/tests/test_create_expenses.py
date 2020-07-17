import os

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import ExpenseUser


dir_path = os.path.dirname(os.path.realpath(__file__))


class JwtExpenseUserTest(TestCase):
    fixtures = [f'{dir_path}/fixtures/created_expenses.json', ]

    def setUp(self) -> None:
        self.test_client = Client()
        self.test_api_client = APIClient()
        self.jhon_exp = ExpenseUser.objects.get(pk=4)
        self.jhon_exp.set_password("abcdefg")
        self.jhon_exp.save()

    def test_get_expenses_unauthorize(self):

        test_url = reverse('expenses_urls:user_expenses')
        test_request = self.test_client.get(test_url)
        self.assertEqual(test_request.status_code, 401)

    def test_post_expenses_unauthorize(self):
        expense_data = {
            'expense_type': 'food',
            'cost': 5000
        }
        test_url = reverse('expenses_urls:user_expenses')
        test_request = self.test_client.post(test_url, expense_data)
        self.assertEqual(test_request.status_code, 401)

    def test_post_expenses(self):

        jhon_data = {
            "username": "jhon.lenon-expe@test.com",
            "password": "abcdefg",
        }

        expense_data = {
            'expense_type': 'food',
            'cost': 5000
        }

        test_url = reverse('users_urls:token_obtain_pair')
        jwt_reponse = self.test_client.post(test_url, jhon_data)

        test_url = reverse('expenses_urls:user_expenses')
        token = jwt_reponse.data.get('access')

        self.test_api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        test_request = self.test_api_client.post(
            test_url,
            expense_data,
            format='json'
        )
        self.assertEqual(test_request.status_code, 201)

    def test_get_expenses(self):
        jhon_data = {
            "username": "jhon.lenon-expe@test.com",
            "password": "abcdefg",
        }
        test_url = reverse('users_urls:token_obtain_pair')
        jwt_reponse = self.test_client.post(test_url, jhon_data)

        test_url = reverse('expenses_urls:user_expenses')
        token = jwt_reponse.data.get('access')

        self.test_api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        test_request = self.test_api_client.get(test_url)

        test_json = test_request.json()

        self.assertEqual(test_request.status_code, 200)
        self.assertEqual(len(test_json), 2)
