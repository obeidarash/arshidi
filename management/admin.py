from django.contrib import admin
from .models import Project, TimeSheet
from .forms import ProjectAdminForm


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'hour_work', 'price', 'project', 'date', 'pk',)
    search_fields = ('project', 'employee',)
    autocomplete_fields = ('project', 'employee',)
    ordering = ('-created',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # fields = ('title', ('budget_type', 'currency'), ('min_budget', 'max_budget', 'fixed_budget'),)
    form = ProjectAdminForm
    list_display = ('__str__', 'deadline', 'status', 'category',)
    autocomplete_fields = ('skills', 'employees', 'contact', 'company',)
    search_fields = ('title',)
    list_filter = ('status', 'category', 'budget_type', 'deadline',)
    ordering = ('-created',)
    filter_horizontal = ('skills',)
