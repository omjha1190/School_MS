from django.db import models
from students.models import Student

# Create your models here.
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, default="Pending")

    def __str__(self):
        return f"{self.student} - {self.fee_type}"
    