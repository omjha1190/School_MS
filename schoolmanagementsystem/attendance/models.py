from django.db import models

# Create your models here.
class StudentAttendance(models.Model):
    enrollment = models.ForeignKey("academics.StudentEnrollment", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["enrollment", "date"],
                name="unique_enrollment_attendance_per_day"
            )
        ]

    def __str__(self):
        return f"{self.enrollment.student} - {self.date}"


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "date"],
                name="unique_teacher_attendance_per_day"
            )
        ]

    def __str__(self):
        return f"{self.teacher} - {self.date}"
    