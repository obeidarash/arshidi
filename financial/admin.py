from django.contrib import admin
from .models import Expense, Income, Salary


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'to', 'price', 'currency', 'date')
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    autocomplete_fields = ('project',)
    ordering = ("-created",)
    date_hierarchy = "date"


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'price', 'currency', 'date',)
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    autocomplete_fields = ('employee', 'project',)
    ordering = ("-created",)
    date_hierarchy = "date"


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'price', 'currency', 'date',)
    search_fields = ('title',)
    autocomplete_fields = ('project',)
    list_filter = ('currency', 'date',)
    ordering = ("-created",)
    date_hierarchy = "date"
