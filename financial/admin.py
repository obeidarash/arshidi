from django.contrib import admin
from .models import Expense, Income, Salary


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'to', 'price', 'currency', 'date')
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    # autocomplete_fields = ('project',)


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'price', 'currency',)
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    # autocomplete_fields = ('employee', 'project',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency',)
    search_fields = ('title',)
    # autocomplete_fields = ('project',)
    list_filter = ('currency', 'date',)
