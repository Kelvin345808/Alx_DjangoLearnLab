# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# Output: 1984 George Orwell 1949
```
