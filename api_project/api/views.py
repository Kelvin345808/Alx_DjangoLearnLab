from rest_framework.generics import ListAPIView  
from .models import Book
from .serializers import BookSerializer

# Define the BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
