from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
