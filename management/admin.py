from django.contrib import admin
from .models import Project, Skill, Freelancer, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email',)
    autocomplete_fields = ('skills', 'positions',)
    search_fields = ('firstname', 'lastname', 'email', 'phone',)
    list_filter = ('positions',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status',)
    autocomplete_fields = ('skills', 'freelancers',)
    search_fields = ('title',)
    list_filter = ('status',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ['title', ]}
