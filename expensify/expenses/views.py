"""
expenses.views
--------------
API views for expenses app
"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Expense
from .serializers import UserExpenseSerializer


class ExpenseListView(ModelViewSet):
    queryset = Expense.get_all()
    serializer_class = UserExpenseSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
