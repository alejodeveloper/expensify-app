"""
expenses.urls
----------
Handle the urls for the users app
"""

from django.urls import path
from . import views

app_name = 'expenses_urls'

urlpatterns = [
    path(
        'expenses/',
        views.ExpenseListView.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ),
        name='user_expenses'
    ),
    path(
        'expenses/<str:expense_id>',
        views.ExpenseListView.as_view({'get': 'retrieve'}),
        name='detail_expense'
    ),
]
