"""
users.serializers
-----------------
Serializers to handle users app
"""

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ExpenseUser


class ExpenseUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ExpenseUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'token'
        )

    def get_token(self, app_user):
        refresh = RefreshToken.for_user(app_user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.get('email')
        username = self.initial_data.get('username')

        already_user_email = self.Meta.model.objects.filter(email=email)
        already_user_username = self.Meta.model.objects.filter(
            username=username
        )

        if already_user_email.exists() or already_user_username.exists():
            error_message = f'User with email {email} or username {username}' \
                f' already exists'
            raise ValidationError(error_message)

        app_user = self.Meta.model(**validated_data)

        if password is not None:
            app_user.set_password(password)
            app_user.save()
            return app_user

