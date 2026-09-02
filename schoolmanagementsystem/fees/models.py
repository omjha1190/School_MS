from django.db import models
from students.models import Student
from academics.models import SchoolClass, Section

# Create your models here.

class FeeItem(models.Model):
    FEE_TYPES = [
        ("Tuition", "Tuition Fee"),
        ("Admission", "Admission Fee"),
        ("Registration", "Registration Fee"),
        ("Annual", "Annual Fee"),
        ("Examination", "Examination Fee"),
        ("Transport", "Transport Fee"),
        ("Library", "Library Fee"),
        ("Computer/Lab", "Computer/Lab Fee"),
        ("Activity", "Activity Fee"),
        ("Sports", "Sports Fee"),
        ("Miscellaneous", "Miscellaneous Fee"),
        ("Late", "Late Fee"),
        ("Hostel", "Hostel Fee"),
    ]
    fee_type = models.CharField(max_length=100, choices=FEE_TYPES)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fee_type} - {self.schoolclass.name} - {self.amount}"

    
class Fee(models.Model):
    FEE_STATUS = [
        ("Pending", "Pending"),
        ("Partial", "Partial"),
        ("Paid", "Paid"),
        ("Overdue", "Overdue"),
    ]
    PAYMENT_METHODS = [
        ("Cash","Cash"),
        ("Bank Transfer","Bank Transfer"),
        ("UPI","UPI"),
        ("Cheque","Cheque"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_items = models.ManyToManyField(FeeItem, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=FEE_STATUS, default="Pending")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS, default="Cash" , null=True, blank=True)

    @property
    def total_amount(self):
        return sum(item.amount for item in self.fee_items.all())

    def __str__(self):
        return f"{self.student} - {self.total_amount}"

    