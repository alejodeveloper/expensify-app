"""
users.views
-----------
API Views for the users app
"""
# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import ExpenseUser
from .serializers import ExpenseUserSerializer


class ExpenseUserViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ExpenseUserSerializer
    queryset = ExpenseUser.get_all()

    def create(self, request, *args, **kwargs):
        serializer = ExpenseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
