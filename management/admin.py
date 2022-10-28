from django.contrib import admin
from .models import Project, TimeSheet
from .forms import ProjectAdminForm


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('project', 'employee', 'date', 'pk',)
    search_fields = ('project', 'employee',)
    autocomplete_fields = ('project', 'employee',)
    ordering = ('-created',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('__str__', 'status',)
    autocomplete_fields = ('skills', 'employees', 'contact', 'company',)
    search_fields = ('title',)
    list_filter = ('status', 'budget_type',)
    ordering = ('-created',)
