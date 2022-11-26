from django.contrib import admin
from .models import Expense, Income, Salary, BankAccount, Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ['name', ]}
    ordering = ('-created',)
    list_per_page = 20


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ('owner',)
    list_display = ('owner', 'bank', 'card_number')
    autocomplete_fields = ('owner', 'bank',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'to', 'price', 'currency', 'source', 'payer', 'date')
    search_fields = ('title',)
    list_filter = ('currency', 'source', 'payer', 'date',)
    autocomplete_fields = ('project', 'payer',)
    ordering = ("-date",)
    date_hierarchy = "date"
    radio_fields = {
        'source': admin.HORIZONTAL,
        'currency': admin.HORIZONTAL
    }


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    # fields = (('currency', 'price'), ('employee', 'date'), 'project', 'attach', 'comment')
    list_display = ('employee', 'price', 'currency', 'date', 'advance_payment',)
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    autocomplete_fields = ('employee', 'project', 'bank_account',)
    ordering = ("-date",)
    date_hierarchy = "date"
    radio_fields = {
        'currency': admin.HORIZONTAL
    }


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'price', 'currency', 'date',)
    search_fields = ('title',)
    autocomplete_fields = ('project',)
    list_filter = ('currency', 'date',)
    ordering = ("-date",)
    date_hierarchy = "date"
    radio_fields = {
        'currency': admin.HORIZONTAL
    }
