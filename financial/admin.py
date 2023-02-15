from django.contrib import admin
from .models import Expense, Income, Salary, BankAccount, Bank, Currency, Category
from .fomrs import BankAccountAdminForm


# @admin.register(Wallet)
# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('title', 'network', 'address',)
#     search_fields = ('title',)
#     autocomplete_fields = ('currency',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'crypto',)
    search_fields = ('title', 'code',)
    list_filter = ('crypto',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ['name', ]}
    ordering = ('-created',)
    list_per_page = 20


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    form = BankAccountAdminForm
    search_fields = ('owner', 'email',)
    list_display = ('owner', 'bank', 'card_number', 'email',)
    autocomplete_fields = ('owner', 'bank',)
    list_filter = ('owner',)


def duplicate_event(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.attach = None
        object.save()


duplicate_event.short_description = "Duplicate selected expenses"


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'to', 'currency', 'category', 'payer', 'date')
    search_fields = ('title',)
    list_filter = ('currency', 'source', 'payer', 'date', 'category',)
    autocomplete_fields = ('project', 'payer', 'currency', 'category', 'to',)
    ordering = ("-date",)
    date_hierarchy = "date"
    actions = [duplicate_event]
    radio_fields = {
        'source': admin.HORIZONTAL,
    }


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    # fields = (('currency', 'price'), ('employee', 'date'), 'project', 'attach', 'comment')
    list_display = ('employee', 'price', 'currency', 'date', 'advance_payment',)
    search_fields = ('title',)
    list_filter = ('currency', 'date',)
    autocomplete_fields = ('employee', 'project', 'bank_account', 'currency',)
    ordering = ("-date",)
    date_hierarchy = "date"


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('project', 'price', 'currency', 'date',)
    search_fields = ('project',)
    autocomplete_fields = ('project', 'currency', 'bank',)
    list_filter = ('currency', 'date',)
    ordering = ("-date",)
    date_hierarchy = "date"
