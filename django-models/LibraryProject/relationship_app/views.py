from django.shortcuts import render
from .models import Book, Library  

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library  # Ensure Library model is used
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
