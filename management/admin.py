from django.contrib import admin
from .models import Project, TimeSheet
from .forms import ProjectAdminForm


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'hour_work', 'payment_method', 'payment', 'currency', 'project', 'date', 'pk',)
    search_fields = ('project', 'employee',)
    autocomplete_fields = ('project', 'employee',)
    ordering = ('-created',)
    radio_fields = {
        'currency': admin.HORIZONTAL,
        'payment_type': admin.HORIZONTAL,
    }

    def payment(self, obj):
        if obj.payment_hourly:
            return obj.payment_hourly
        return obj.payment_fixed

    def payment_method(self, obj):
        if obj.payment_type == 'hour':
            return "Hourly"
        return "Fixed"


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
    radio_fields = {
        'experience_level': admin.HORIZONTAL,
        'budget_type': admin.HORIZONTAL,
        'project_type': admin.HORIZONTAL,
        'currency': admin.HORIZONTAL,
        # 'category': admin.HORIZONTAL,
    }
