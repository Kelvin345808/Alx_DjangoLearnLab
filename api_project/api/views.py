from rest_framework.generics import ListAPIView  
from .models import Book
from .serializers import BookSerializer

# Define the BookList view
class BookList("generics.ListAPIView"):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
