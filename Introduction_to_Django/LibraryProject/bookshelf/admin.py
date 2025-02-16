# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Customizing the Book model admin interface
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to be searchable
    search_fields = ('title', 'author')
    
    # Adding filters for the publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)
