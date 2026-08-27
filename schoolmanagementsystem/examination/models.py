from django.db import models
from academics.models import SchoolClass, Subject, Section
from students.models import Student

# Create your models here.
class Exam(models.Model):
    EXAM_MODE = [
        ("Offline", "Offline"),
        ("Online", "Online")
    ]
    EXAM_STATUS = [
        ("Upcoming", "Upcoming"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed")
    ]
    exam_name = models.CharField(max_length=200)
    schoolclass = models.ManyToManyField(SchoolClass)
    academic_year = models.CharField(max_length=20)
    mode = models.CharField(max_length=20, choices=EXAM_MODE ,default="Offline")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=EXAM_STATUS ,default="Upcoming")
    instructions = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.exam_name


class ExamSchedule(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=100)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.exam.exam_name} - {self.section} - {self.subject}"

class Result(models.Model):
    GRADE_CHOICES = [
        ("A+", "A+"),
        ("A", "A"),
        ("B+", "B+"),
        ("B", "B"),
        ("C+", "C+"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F")
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "exam", "subject"],
                name="unique_student_exam_subject"
            )
        ]    

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"
        