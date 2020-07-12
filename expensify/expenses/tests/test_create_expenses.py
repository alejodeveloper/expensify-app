import os

from django.test import Client, TestCase
from django.urls import reverse
from expenses.models import Expense
from users.models import ExpenseUser


dir_path = os.path.dirname(os.path.realpath(__file__))


class JwtExpenseUserTest(TestCase):
    fixtures = [f'{dir_path}/fixtures/created_expenses.json', ]

    def setUp(self) -> None:
        self.test_client = Client()
        self.jhon = ExpenseUser.objects.get(pk=1)
        self.jhon.set_password("abcdefg")
        self.test_expense = Expense.objects.get(user=self.jhon)

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
            "username": "jhon.lenon@test.com",
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
        auth_header = {'Authorization': f'Bearer {token}'}

        test_request = self.test_client.post(
            test_url,
            expense_data,
            **auth_header
        )
        self.assertEqual(test_request.status_code, 201)

    def test_get_expenses(self):
        jhon_data = {
            "username": "jhon.lenon@test.com",
            "password": "abcdefg",
        }
        test_url = reverse('users_urls:token_obtain_pair')
        jwt_reponse = self.test_client.post(test_url, jhon_data)

        test_url = reverse('expenses_urls:user_expenses')
        token = jwt_reponse.data.get('access')
        auth_header = {'Authorization': f'Bearer {token}'}
        test_request = self.test_client.post(test_url, **auth_header)

        test_json = test_request.json()

        self.assertEqual(test_request.status_code, 200)
        self.assertEqual(len(test_json.get('expenses')), 2)
