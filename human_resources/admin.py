from django.contrib import admin
from .models import Position, Skill, Employee, Hire
from django.utils.html import format_html


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}
    ordering = ('-title',)


@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'interview_date', 'potential', 'interviewed', 'rate')
    autocomplete_fields = ('skills', 'positions', 'currency',)
    search_fields = ('firstname', 'lastname', 'email', 'phone',)
    list_filter = ('positions', 'potential', 'interviewed',)
    ordering = ('-positions',)
    radio_fields = {
        'gender': admin.HORIZONTAL,
    }


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active',)
    autocomplete_fields = ('skills', 'positions',)
    search_fields = ('firstname', 'lastname', 'email', 'phone',)
    search_help_text = "Search in firstname, lastname, email and phone"
    list_filter = ('positions', 'is_active',)
    ordering = ('-lastname',)
    filter_horizontal = ['positions']
    radio_fields = {
        'gender': admin.HORIZONTAL,
    }

    # def email_link(self, obj):
    #     return format_html("<a href='mailto:{}' target='_blank'>{}</a>", obj.email, obj.email)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}
    ordering = ('-created',)
    list_per_page = 20
