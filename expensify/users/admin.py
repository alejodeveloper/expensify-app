from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ExpenseUser


class ExpenseUserAdmin(UserAdmin):

    model = ExpenseUser
    list_display = (
        'first_name',
        'last_name',
        'email',
        'user_type',
        'is_staff',
        'is_active',
    )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (
            None, {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'user_type',
                    'password'
                )
            }
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )
    search_fields = ('email', 'user_type',)
    ordering = ('email',)


admin.site.register(ExpenseUser, ExpenseUserAdmin)
