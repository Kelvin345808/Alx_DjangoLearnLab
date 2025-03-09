from rest_framework.generics import ListAPIView  
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Define the BookList view
class BookList("generics.ListAPIView"):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer