from django.db import models
from academics.models import Subject, Section
from students.models import Student

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = [
        ("Textbook", "Textbook"),
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Story Book", "Story Book"),
        ("Novel", "Novel"),
        ("Biography", "Biography"),
        ("Autobiography", "Autobiography"),
        ("Poetry", "Poetry"),
        ("Comics", "Comics"),
        ("Dictionary", "Dictionary"),
        ("Atlas", "Atlas"),
        ("Encyclopedia", "Encyclopedia"),
        ("Other", "Other"),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="books/", null=True, blank=True)
    isbn = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    publisher = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=1)
    available_quantity = models.IntegerField(default=1)
    shelf_number = models.CharField(max_length=50,null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BookIssue(models.Model):
    ISSUE_STATUS = [
        ("Issued", "Issued"),
        ("Returned", "Returned"),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default="Issued")

    def __str__(self):
        return f"{self.student} - {self.book.title}"
    