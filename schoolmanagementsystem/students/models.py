from django.db import models
from django.contrib.auth.models import User
from academics.models import SchoolClass, Section

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', "Male"),
        ('Female', "Female"),
        ('other', "other")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='student_covers/', null=True, blank=True)
    admission_number = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    admission_date = models.DateField()
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, null=True,blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.user.get_full_name()
    