from django.db import models
from academics.models import SchoolClass, Subject
from students.models import Student

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=200)
    schoolclass = models.ManyToManyField(SchoolClass)
    date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject.name} - {self.marks}"
    
