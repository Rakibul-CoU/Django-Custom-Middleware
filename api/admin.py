from django.contrib import admin

from api.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]

admin.site.register(Book, BookAdmin)
