"""
expenses.admin
--------------
Admin models and actions for expenses models
"""
# Register your models here.
from django.contrib import admin

from . import models


class ExpenseTypeAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'slug',
    )
    list_display = (
        'name',
        'slug',
    )

    search_fields = [
        'name',
        'slug',
    ]


class ExpenseAdmin(admin.ModelAdmin):

    fields = (
        'user',
        'expense_id',
        'expense_name',
        'expense_type',
        'cost',
        'expense_date',
    )
    list_display = (
        'user',
        'expense_id',
        'expense_name',
        'expense_type',
        'cost',
        'expense_date',
        'created_at',
        'updated_at',
    )

    search_fields = [
        'user__username',
        'user__email',
        'expense_type__slug',
        'expense_type__name',
        'expense_date',
    ]


admin.site.register(models.Expense, ExpenseAdmin)
admin.site.register(models.ExpenseType, ExpenseTypeAdmin)


