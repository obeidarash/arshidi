from django.contrib import admin
from .models import Project, Category
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # fields = ('title', ('budget_type', 'currency'), ('min_budget', 'max_budget', 'fixed_budget'),)
    list_display = ('__str__', 'deadline', 'status', 'get_contacts', 'get_companies', 'budget', 'payment',)
    autocomplete_fields = ('skills', 'employees', 'contact', 'company', 'Category')
    search_fields = ('title',)
    list_filter = ('payment', 'Category', 'status', 'budget_type', 'deadline',)
    ordering = ('-created',)
    filter_horizontal = ('skills',)
    radio_fields = {
        'budget_type': admin.HORIZONTAL,
        # 'project_type': admin.HORIZONTAL,
        'currency': admin.HORIZONTAL,
        # 'category': admin.HORIZONTAL,
    }
    

    def get_companies(self, obj):
        return format_html(f'<a href="/admin/contacts/company/{obj.company.id}/change/">{obj.company.name}</a>')
    get_companies.short_description = "Companies"

    def get_contacts(self, obj):
        return format_html(",\n".join([f'<a href="/admin/contacts/contact/{p.id}/change/">{p.firstname} {p.lastname}</a>' for p in obj.contact.all()]))
    get_contacts.short_description = "contacts"
