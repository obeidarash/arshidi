from django.contrib import admin
from .models import File, Library


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
    list_display = ('title', 'file',)
    # autocomplete_fields = ('category',)
    search_fields = ('title',)
    ordering = ('-created',)
