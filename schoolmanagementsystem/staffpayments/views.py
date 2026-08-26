from django.shortcuts import render, redirect
from .models import StaffPayment
from staffs.models import Staff
from decimal import Decimal

# Create your views here.
def insert_staffpayment(req):
    data ={
        "staffs" : Staff.objects.all(),
        "payment_status" : StaffPayment.PAYMENT_STATUS,
        "payment_methods" : StaffPayment.PAYMENT_METHOD
    }
    if req.method == "POST":
        payment = StaffPayment()
        payment.staff = Staff.objects.get(id=req.POST.get('staff'))
        payment.basic_salary = Decimal(req.POST.get("basic_salary"))
        payment.allowances = Decimal(req.POST.get("allowances") or 0)
        payment.deductions = Decimal(req.POST.get("deductions") or 0)

        payment.net_salary = (payment.basic_salary + payment.allowances - payment.deductions)

        payment.payment_date = req.POST.get('payment_date') or None
        payment.status = req.POST.get('status')
        payment.payment_method = req.POST.get('payment_method')
        payment.notes = req.POST.get('notes') or None
        payment.save()
        return redirect("manage_staffpayments")
    return render(req, "staffpayments/insert_staffpayment.html", data)

def manage_staffpayments(req):
    data = {
        "payments" : StaffPayment.objects.all(),
    }
    return render(req, "staffpayments/manage_staffpayments.html", data)


def edit_staffpayment(req, id):
    data = {
        "staffs" : Staff.objects.all(),
        "payment_status" : StaffPayment.PAYMENT_STATUS,
        "payment_methods" : StaffPayment.PAYMENT_METHOD,
        "payment" : StaffPayment.objects.get(id=id)
    }
    if req.method == "POST":
        payment = StaffPayment.objects.get(id=id)
        payment.staff = Staff.objects.get(id=req.POST.get('staff'))
        payment.basic_salary = Decimal(req.POST.get('basic_salary'))
        payment.allowances = Decimal(req.POST.get('allowances'))
        payment.deductions = Decimal(req.POST.get('deductions'))
        payment.payment_date = req.POST.get('payment_date') or None
        payment.status = req.POST.get('status')
        payment.payment_method = req.POST.get('payment_method')
        payment.notes = req.POST.get('notes')
        payment.save()
        return redirect("manage_staffpayments")

    return render(req, "staffpayments/insert_staffpayment.html", data)

def delete_staffpayment(req, id):
    data = {}
    try :
        staffpayment = StaffPayment.objects.get(id=id)
        staffpayment.delete()
        return redirect("manage_staffpayments")
    except StaffPayment.DoesNotExist:
        data ['error'] = "This Payment is not available"
    return redirect("manage_staffpayments")


def staffpayment_history(req, id):
    staff = Staff.objects.get(id=id)
    data = {
        "staff" : staff,
        "payments" : StaffPayment.objects.filter(staff=staff)
    }
    return render(req, "staffpayments/staffpayment_history.html", data)