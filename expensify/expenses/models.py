import uuid

from django.db import models

from users.models import ExpenseUser
from .constants import ExpenseTypeSlug
# Create your models here.


class ExpenseType(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    slug = models.CharField(
        blank=False,
        null=False,
        choices=ExpenseTypeSlug.choices()
    )


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
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
