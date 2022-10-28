from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file',)
    search_fields = ('title',)
    autocomplete_fields = ("employee", )


