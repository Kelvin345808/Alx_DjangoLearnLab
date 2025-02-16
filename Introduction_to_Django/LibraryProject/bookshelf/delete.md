# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
retrieved_book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
# Output: <QuerySet []>
```
