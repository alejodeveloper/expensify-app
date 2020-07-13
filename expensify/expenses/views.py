"""
expenses.views
--------------
API views for expenses app
"""
from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.authentication import JWTAuthentication

from .constants import GeneralConstants, ExpenseTypeSlug
from .models import Expense, ExpenseType
from .serializers import UserExpenseSerializer


class ExpenseListView(ModelViewSet):
    queryset = Expense.get_all()
    serializer_class = UserExpenseSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def create(self, request, *args, **kwargs):
        expense_user = request.user
        create_data = request.data

        expense_date = self.validate_expense_date(
            create_data.get('expense_date')
        )
        expense_type = self.validate_expense_type(
            create_data.get('expense_type')
        )
        create_data.update(
            user=expense_user.id,
            expense_date=expense_date,
            expense_type=expense_type.id,
        )
        serializer = UserExpenseSerializer(data=create_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def validate_expense_date(self, value) -> datetime:
        """
        Validate the date for the expense
        :param value: the date for expense
        :return: datetime value for the expense
        """
        if value is None:
            return datetime.now()

        return datetime.strptime(value, GeneralConstants.DATE_STRFORMAT.value)

    def validate_expense_type(self, value) -> ExpenseType:
        """
        Validate if the value is on one of the choices
        :param value: str with the type expense value
        """
        if ExpenseTypeSlug.get_values().get(value):
            return ExpenseType.get_expense_type(value)
