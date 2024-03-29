from django.contrib import admin
from .models import Expense, Income, Salary, BankAccount, Bank, Currency, Category
from .fomrs import BankAccountAdminForm, SalaryAdminForm
from django.utils.html import format_html


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
    list_display = ('title', 'price', 'get_companies', 'category', 'currency', 'date')
    search_fields = ('title', 'comment', )
    list_filter = ('currency', 'source', 'payer', 'date', 'category',)
    autocomplete_fields = ('project', 'payer', 'currency', 'category', 'to',)
    ordering = ("-date",)
    date_hierarchy = "date"
    actions = [duplicate_event]
    radio_fields = {
        'source': admin.HORIZONTAL,
    }


    def get_companies(self, obj):
        if obj.to:
            return format_html(f'<a target="_blank" href="/admin/contacts/company/{obj.to.id}/change/">{obj.to.name}</a>')
        return '-'
    get_companies.short_description = "Companies"

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    form = SalaryAdminForm
    # fields = (('currency', 'price'), ('employee', 'date'), 'project', 'attach', 'comment')
    list_display = ('get_name', 'price', 'currency', 'date', 'advance_payment',)
    search_fields = ('title',)
    list_filter = ('currency', 'date', 'employee', )
    autocomplete_fields = ('employee', 'project', 'bank_account', 'currency', 'contact', 'company', )
    ordering = ("-date",)
    date_hierarchy = "date"

    def get_name(self, obj):
        if obj.employee:
            return f"{obj.employee.firstname} {obj.employee.lastname}"
        elif obj.contact:
            return f"{obj.contact.firstname} {obj.contact.lastname}"
        elif obj.company:
            return f"{obj.company.name}"
        return '-'
    get_name.short_description = "Name"


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('project', 'price', 'currency', 'date',)
    search_fields = ('project',)
    autocomplete_fields = ('project', 'currency', 'bank',)
    list_filter = ('currency', 'date',)
    ordering = ("-date",)
    date_hierarchy = "date"
