from django.shortcuts import render, redirect
from .models import Book
from academics.models import Subject

# Create your views here.
def insert_book(req):
    data = {
        "subjects" : Subject.objects.all(),
        "categories" : Book.CATEGORY_CHOICES
    }
    if req.method == "POST":
        book = Book()
        book.title = req.POST.get('title')
        book.author = req.POST.get('author')
        book.isbn = req.POST.get('isbn')
        book.category = req.POST.get('category')
        book.publisher = req.POST.get('publisher')
        book.quantity = req.POST.get('quantity')
        book.available_quantity = req.POST.get('quantity')
        book.shelf_number = req.POST.get('shelf_number')
        book.subject_id = req.POST.get('subject') or None 
        book.cover_image = req.FILES.get('cover_image')
        book.description = req.POST.get('description')
        book.save()
        return redirect("manage_books")
    return render(req, "library/insert_book.html", data)

def manage_books(req):
    data = {
        "books" : Book.objects.all()
    }
    return render(req, "library/manage_books.html", data)

def book_details(req, id):
    data = {
        "book" : Book.objects.get(id=id)
    }
    return render(req, "library/book_details.html", data)

def edit_book(req, id):
    book = Book.objects.get(id=id)
    data = {
        "book" : book,
        "subjects" : Subject.objects.all(),
        "categories" : Book.CATEGORY_CHOICES
    }
    if req.method == "POST":
        book.title = req.POST.get('title')
        book.author = req.POST.get('author')
        book.cover_image = req.FILES.get('cover_image')
        book.isbn = req.POST.get('isbn')
        book.category = req.POST.get('category')
        book.publisher = req.POST.get('publisher')
        book.quantity = req.POST.get('quantity')
        book.available_quantity = req.POST.get('quantity')
        book.shelf_number = req.POST.get('shelf_number')
        book.subject.id = req.POST.get('subject') or None
        book.description = req.POST.get('description')
        book.save()
        return redirect("manage_books")
    return render(req, "library/insert_book.html", data)

def delete_book(req, id):
    data = {}
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("manage_books")
    except Book.DoesNotExist:
        data ['error'] = "This Book does not exist"
    return redirect("manage_books")
