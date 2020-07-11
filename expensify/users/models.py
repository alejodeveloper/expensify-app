"""
users.models
------------
Class models for users app
"""
# Create your models here.
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError

from .constants import UserTypes


class ExpenseUser(AbstractUser):
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        null=False,
        blank=False,
    )
    user_type = models.CharField(
        choices=UserTypes.choices(),
        default=UserTypes.FREE.value,
        max_length=25,
        blank=False,
        null=False,
    )
    # add additional fields in here

    def __str__(self):
        return self.username

    @classmethod
    def get_all(cls):
        """
        Returns the objects.all() queryset for the model
        :return: queryset
        """
        return cls.objects.all()
