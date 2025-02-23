from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure Library is imported


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library  # Ensure Library model is used
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
