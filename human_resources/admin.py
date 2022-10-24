from django.contrib import admin
from .models import Position, Skill, Freelancer
from django.utils.html import format_html


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email_link',)
    autocomplete_fields = ('skills', 'positions',)
    search_fields = ('firstname', 'lastname', 'email', 'phone',)
    list_filter = ('positions',)

    def email_link(self, obj):
        return format_html("<a href='mailto:{}' target='_blank'>{}</a>", obj.email, obj.email)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}
