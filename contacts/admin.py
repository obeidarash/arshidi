from django.contrib import admin
from .models import Contact, Company


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname',)
    search_fields = ('firstname', 'lastname',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    autocomplete_fields = ('contact', )
