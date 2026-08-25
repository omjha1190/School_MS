from django.shortcuts import render, redirect
from .models import Staff

# Create your views here.
def insert_staff(req):
    data = {
        "staff_types" : Staff.STAFF_TYPES, 
        "gender_choices" : Staff.GENDER_CHOICES
    }
    if req.method == "POST":
        staff = Staff()
        staff.name = req.POST.get('name')
        staff.cover_image = req.FILES.get('cover_image')
        staff.address = req.POST.get('address')
        staff.staff_type = req.POST.get('staff_type')
        staff.gender = req.POST.get('gender')
        staff.phone = req.POST.get('phone')
        staff.email = req.POST.get('email') or None
        staff.joining_date = req.POST.get('joining_date')
        staff.salary = req.POST.get('salary')
        staff.save()
        return redirect("manage_staffs")
    return render(req, "staff/insert_staff.html", data)


def manage_staffs(req):
    data = {
        "staffs" : Staff.objects.all(),
    }
    return render(req, "staff/manage_staffs.html", data)