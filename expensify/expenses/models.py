"""
expenses.models
---------------
Class Models for expenses app
"""
import uuid

from django.db import models

from users.models import ExpenseUser
from .constants import ExpenseTypeSlug
# Create your models here.


class ExpenseType(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    slug = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        choices=ExpenseTypeSlug.choices()
    )

    def __str__(self):
        return f"{self.slug.name}"


class Expense(models.Model):
    expense_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        null=False,
        blank=False,
    )
    expense_name = models.CharField(blank=True, null=True, max_length=255)
    expense_type = models.ForeignKey(
        ExpenseType,
        related_name="expenses",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    cost = models.DecimalField(
        null=False,
        blank=False,
        max_digits=19,
        decimal_places=2
    )
    user = models.ForeignKey(
        ExpenseUser,
        related_name="expenses",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    expense_date = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user_id"]),
            models.Index(fields=["user_id", "expense_date"]),
            models.Index(fields=["user_id", "expense_id"]),
            models.Index(fields=["user_id", "expense_type"]),
        ]

    @classmethod
    def get_all(cls):
        """
        Get all the objects and return a queryset
        :return: queryset with all query objects
        """
        return cls.objects.all()
