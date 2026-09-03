from django.shortcuts import render, redirect
from .models import Book, BookIssue
from academics.models import Subject, Section
from students.models import Student
from datetime import date

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


def insert_book_issue(req):
    data = {
        "books" : Book.objects.all(),
        "students" : Student.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        book = Book.objects.get(id=req.POST.get('book'))

        if book.available_quantity <= 0:
            data ['error'] = "The book is not available."
            return render(req, "library/insert_book_issue.html", data)
        
        bookissue = BookIssue()
        bookissue.book_id=req.POST.get('book')
        bookissue.student_id=req.POST.get('student')
        bookissue.section_id=req.POST.get('section')
        bookissue.issue_date=req.POST.get('issue_date')
        bookissue.due_date=req.POST.get('due_date')
        bookissue.save()

        book.available_quantity -=1
        book.save()

        return redirect("manage_book_issues")
    return render(req, "library/insert_book_issue.html", data)

def manage_book_issues(req):
    data = {
        "bookissues" : BookIssue.objects.all(),
    }
    return render(req, "library/manage_book_issues.html", data)

def return_book(req, id):
    bookissue = BookIssue.objects.get(id=id)

    if bookissue.status == "Issued" :
        bookissue.return_date = date.today()
        bookissue.status = "Returned"
        bookissue.save()

        book = bookissue.book
        book.available_quantity +=1
        book.save()
    return redirect("manage_book_issues")    

def edit_book_issue(req, id):
    bookissue = BookIssue.objects.get(id=id)
    data = {
        "bookissue" : bookissue,
        "books" : Book.objects.all(),
        "students" : Student.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        bookissue.book_id = req.POST.get('book')
        bookissue.student_id = req.POST.get('student')
        bookissue.section_id = req.POST.get('section')
        bookissue.issue_date = req.POST.get('issue_date')
        bookissue.due_date = req.POST.get('due_date')
        bookissue.save()
        return redirect("manage_book_issues")
    return render(req, "library/insert_book_issue.html", data)


def delete_book_issue(req, id):
    data = {}
    try:
        bookissue = BookIssue.objects.get(id=id)
        bookissue.delete()
        return redirect("manage_book_issues")
    except BookIssue.DoesNotExist:
        data ['error'] = "This Book Issue does not exist"
    return redirect("manage_book_issues")