from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the existing ListAPIView (if needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs
    path('', include(router.urls)),  # This includes all routes registered with the router
]