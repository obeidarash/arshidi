from django.contrib import admin
from .models import Project, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # fields = ('title', ('budget_type', 'currency'), ('min_budget', 'max_budget', 'fixed_budget'),)
    list_display = ('__str__', 'deadline', 'status', 'get_contacts', 'budget', 'payment',)
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

    def get_contacts(self, obj):
        return ",\n".join([f'{p.firstname} {p.lastname}' for p in obj.contact.all()])
    get_contacts.short_description = "contacts"
