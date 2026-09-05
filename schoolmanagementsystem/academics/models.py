from django.db import models
from teachers.models import Teacher

# Create your models here.
class SchoolClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Section(models.Model):
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.schoolclass.name} - {self.name}"

class StudentEnrollment(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=50)
    roll_no = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["section", "academic_year", "roll_no"],
                name="unique_roll_no_in_section_year"
            ),
            models.UniqueConstraint(
                fields=["student", "academic_year"],
                name="unique_student_in_academic_year"
            ),
        ]

    def __str__(self):
        return f"{self.student} - {self.section} - {self.roll_no}"



class Subject(models.Model):
    name = models.CharField(max_length=20)
    schoolclasses = models.ManyToManyField(SchoolClass)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_subject_name"
            )
        ]

    def __str__(self):  
        return self.name

class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.user.get_full_name()} - {self.subject.name}"
        