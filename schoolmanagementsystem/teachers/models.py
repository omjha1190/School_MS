from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    cover_image = models.ImageField(upload_to='teacher_covers/', null=True, blank=True)
    is_class_teacher = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
    