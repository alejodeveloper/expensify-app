"""
users.models
------------
Class models for users app
"""
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import UserTypes


class ExpenseUser(AbstractUser):
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
