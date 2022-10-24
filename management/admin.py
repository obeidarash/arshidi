from django.contrib import admin
from .models import Project, TimeSheet


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('project', 'freelancer', 'date', 'pk',)
    search_fields = ('project', 'freelancer',)
    autocomplete_fields = ('project', 'freelancer',)
    ordering = ('-created',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status',)
    autocomplete_fields = ('skills', 'freelancers',)
    search_fields = ('title',)
    list_filter = ('status',)
    ordering = ('-created',)
