from django.contrib import admin
from .models import Contact, Company, Tag
from .forms import ContactAdminForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ('firstname', 'lastname', 'position', 'tag',)
    search_fields = ('firstname', 'lastname',)
    autocomplete_fields = ('tags',)
    list_filter = ('tags',)

    def tag(self, obj):
        return ",\n".join([p.title for p in obj.tags.all()])


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts','tag',)
    autocomplete_fields = ('contact', 'tags',)
    search_fields = ('name',)
    list_filter = ('tags',)

    def tag(self, obj):
        return ",\n".join([p.title for p in obj.tags.all()])

    def contacts(self, obj):
        return ",\n".join([f'{p.firstname} {p.lastname}' for p in obj.contact.all()])
