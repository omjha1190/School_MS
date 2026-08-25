from django.db import models

# Create your models here.
class Staff(models.Model):
    STAFF_TYPES = [
        ("Peon", "Peon"),
        ("Security", "Security"),
        ("Helper", "Helper"),
        ("Librarian", "Librarian"),
        ("Gardener", "Gardener"),
        ("Accountant", "Accountant"),
        ("Other", "Other"),
    ]
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="staff/")
    address = models.TextField()
    staff_type = models.CharField(max_length=50, choices=STAFF_TYPES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    