from django.db import models
from staffs.models import Staff

# Create your models here.
class StaffPayment(models.Model):
    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid")
    ]
    PAYMENT_METHOD =[
        ("Cash", "Cash"),
        ("Bank Transfer", "Bank Transfer"),
        ("UPI", "UPI"),
        ("Cheque", "Cheque"),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default="Pending")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, default="Cash")
    notes = models.TextField(null= True, blank= True)


    def __str__(self):
        return f"{self.staff.name} - {self.net_salary} - {self.status}"
    