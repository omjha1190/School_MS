from django.shortcuts import render, redirect
from students.models import Student
from .models import Fee

# Create your views here.
def insert_fee(req):
    data = {
        "students" : Student.objects.all(),
    }
    if req.method == "POST" :
        fee = Fee()
        fee.student = Student.objects.get(id=req.POST.get('student'))
        fee.fee_type = req.POST.get('fee_type')
        fee.amount = req.POST.get('amount')
        fee.due_date = req.POST.get('due_date')
        fee.paid_date = req.POST.get('paid_date') or None
        fee.status = req.POST.get('status')
        fee.save()
        return redirect("manage_fees")
    return render(req, "fees/insert_fee.html", data)

def manage_fees(req):
    data = {
        "fees" : Fee.objects.all()
    }
    return render(req, "fees/manage_fees.html", data)

def edit_fee(req, id):
    data = {
        "students" : Student.objects.all(), 
        "fee" : Fee.objects.get(id=id)
    }
    if req.method == "POST":
        fee = Fee.objects.get(id=id)
        fee.student = Student.objects.get(id=req.POST.get('student'))
        fee.fee_type = req.POST.get('fee_type')
        fee.amount = req.POST.get('amount')
        fee.due_date = req.POST.get('due_date')
        fee.paid_date = req.POST.get('paid_date')
        fee.status = req.POST.get('status')
        fee.save()
        return redirect("manage_fees")
    return render(req, "fees/insert_fee.html", data)

def delete_fee(req, id):
    data = {}
    try :
        fee = Fee.objects.get(id=id)
        fee.delete()
        return redirect("manage_fees")
    except Fee.DoesNotExist:
        data ['error'] = "This fee is not available"
    return redirect("manage_fees")

def fees_history(req, id):
    student = Student.objects.get(id=id)
    data = {
        "student" : student,
        "fees" : Fee.objects.filter(student=student),
    }   
    return render(req, "fees/fees_history.html", data)