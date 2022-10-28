from django.contrib import admin
from .models import Contact, Company
from .forms import ContactAdminForm


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ('firstname', 'lastname',)
    search_fields = ('firstname', 'lastname',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    autocomplete_fields = ('contact',)
    search_fields = ('name',)
