# bookshelf/admin.py

from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

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

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)