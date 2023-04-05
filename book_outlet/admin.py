from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author")
    list_filter=("rating","author")
admin.site.register(Book,BookAdmin)
