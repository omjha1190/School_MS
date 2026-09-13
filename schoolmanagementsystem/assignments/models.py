from django.db import models
from academics.models import SchoolClass, Subject, Section
from teachers.models import Teacher
# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class AssignmentSubmisssion(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    submitted_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="assignment")
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.assignment.title}"
    
    