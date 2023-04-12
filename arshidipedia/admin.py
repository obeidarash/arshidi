from django.contrib import admin
from .models import File, Library
from django.utils.html import format_html

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     search_fields = ('title',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee', 'file',)
    search_fields = ('title',)
    autocomplete_fields = ("employee",)
    list_filter = ('employee',)
    ordering = ('-created',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'get_link',)
    # autocomplete_fields = ('category',)
    search_fields = ('title',)
    ordering = ('-created',)




    def get_link(self, obj):
        if obj.link:
            return format_html(f'<a href="{obj.link}" target="_balnk">{obj.link}</a>')
        return '-'
    get_link.short_description = "link"
