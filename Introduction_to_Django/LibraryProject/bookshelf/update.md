# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
retrieved_book = Book.objects.get(title="1984")

# Update the book's title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)
# Output: Nineteen Eighty-Four
```
