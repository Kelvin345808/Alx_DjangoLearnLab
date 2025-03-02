from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Book

# Create your views here.

@permission_required("bookshelf.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})

@permission_required("bookshelf.can_create", raise_exception=True)
def create_article(request):
    # Handle article creation
    return render(request, "articles/create.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "articles/edit.html", {"article": article})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("article_list")
 
 @permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, "bookshelf/book_list.html", {"books": books})