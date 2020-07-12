"""
expenses.serializers
--------------------
restframework serializers for expenses app
"""
from rest_framework.serializers import ModelSerializer

from .constants import GeneralConstants
from .models import Expense


class UserExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'expense_id',
            'expense_name',
            'expense_type',
            'cost',
            'expense_date',
        )

    def get_expense_date(self, instance) -> str:
        """
        serialize the field expense_type
        :return: str with serialized value
        """
        return instance.name

    def get_expense_date(self, instance) -> str:
        """
        Returns the date wiht a iso format
        :param instance:
        :return:
        """
        if instance.expense_date is not None:
            return f"{instance.expense_date.strftime(GeneralConstants.DATE_STRFORMAT.name)}"
