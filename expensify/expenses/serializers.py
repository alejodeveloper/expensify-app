"""
expenses.serializers
--------------------
restframework serializers for expenses app
"""

from rest_framework.serializers import ModelSerializer

from .models import Expense


class UserExpenseSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = (
            'user',
            'expense_id',
            'expense_name',
            'expense_type',
            'cost',
            'expense_date',
        )
