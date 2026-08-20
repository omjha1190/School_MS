from django.db import models
from students.models import Student
from teachers.models import Teacher

# Create your models here.
class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.date}"


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher} - {self.date}"
    