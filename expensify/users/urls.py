"""
users.urls
----------
Handle the urls for the users app
"""

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = 'users_urls'

urlpatterns = [
    path(
        'token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'expense-user/',
        views.ExpenseUserViewSet.as_view({'post': 'create'}),
        name='expense_app_user'
    )
]
