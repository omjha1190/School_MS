from django.shortcuts import render, redirect
from students.models import Student
from academics.models import SchoolClass, Section
from .models import Fee, FeeItem

# Create your views here.
def insert_fee(req):
    data = {
        "students" : Student.objects.all(),
        "sections" : Section.objects.all(),
        "feeitems" : FeeItem.objects.all(),
        "fee_status" : Fee.FEE_STATUS,
        "payment_methods" : Fee.PAYMENT_METHODS
    }
    if req.method == "POST" :
        fee = Fee()
        fee.student = Student.objects.get(id=req.POST.get('student'))
        fee.section = Section.objects.get(id=req.POST.get('section')) or None
        fee.due_date = req.POST.get('due_date')
        fee.paid_date = req.POST.get('paid_date') or None
        fee.status = req.POST.get('status')
        fee.payment_method = req.POST.get('payment_method') or None
        fee.save()
        fee.fee_items.set(req.POST.getlist('fee_items'))
        return redirect("manage_fees")
    return render(req, "fees/insert_fee.html", data)

def manage_fees(req):
    data = {
        "fees" : Fee.objects.all()
    }
    return render(req, "fees/manage_fees.html", data)

def edit_fee(req, id):
    fee = Fee.objects.get(id=id)
    data = {
        "students" : Student.objects.all(),
        "sections" : Section.objects.all(),
        "feeitems" : FeeItem.objects.all(),
        "fee_status" : Fee.FEE_STATUS,
        "payment_methods" : Fee.PAYMENT_METHODS,
        "fee" : fee
    }
    if req.method == "POST":
        fee.student_id = req.POST.get('student')
        fee.section_id = req.POST.get('section') or None
        fee.due_date = req.POST.get('due_date')
        fee.paid_date = req.POST.get('paid_date') or None
        fee.status = req.POST.get('status')
        fee.payment_method = req.POST.get('payment_method') or None
        fee.save()
        fee.fee_items.set(req.POST.getlist('fee_items'))
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

def insert_feeitem(req):
    data = {
        "fee_types" : FeeItem.FEE_TYPES,
        "schoolclasses" : SchoolClass.objects.all()
    }
    if req.method == "POST":
        feeitem = FeeItem()
        feeitem.fee_type = req.POST.get('fee_type')
        feeitem.schoolclass = SchoolClass.objects.get(id=req.POST.get('schoolclass'))
        feeitem.amount = req.POST.get('amount')
        feeitem.save()
        return redirect("manage_feeitems")
    return render(req, "fees/insert_feeitem.html", data)

def manage_feeitems(req):
    data = {
        "feeitems" : FeeItem.objects.all()
    }
    return render(req, "fees/manage_feeitems.html", data)

def edit_feeitems(req, id):
    data = {
        "feeitem" : FeeItem.objects.get(id=id),
        "fee_types" : FeeItem.FEE_TYPES,
        "schoolclasses" : SchoolClass.objects.all(),
    }
    if req.method == "POST":
        feeitem = FeeItem.objects.get(id=id)
        feeitem.fee_type = req.POST.get('fee_type')
        feeitem.schoolclass = SchoolClass.objects.get(id=req.POST.get('schoolclass'))
        feeitem.amount = req.POST.get('amount')
        feeitem.save()
        return redirect("manage_feeitems")
    return render(req, "fees/insert_feeitem.html", data)

def delete_feeitem(req, id):
    data = {}
    try :
        feeitem = FeeItem.objects.get(id=id)
        feeitem.delete()
        return redirect("manage_feeitems")
    except FeeItem.DoesNotExist:
        data ['error'] = "This Fee item is not availabel"
    return redirect("manage_feeitems")