from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .models import Student
from academics.models import SchoolClass, Section

# Create your views here.
def insert_student(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        user = User()
        user.first_name = req.POST.get("first_name")
        user.last_name = req.POST.get("last_name")
        user.username = req.POST.get("username")
        user.email = req.POST.get("email")
        user.password = req.POST.get("password")
        user.confirm_password = req.POST.get("confirm_password")
        if user.password != user.confirm_password:
            data["error"] = "Password do not match"
            return render(req, "students/insert.html", data)
        user.set_password(user.password)
        user.save()

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.role = "student"
        user_profile.save()

        student = Student()
        student.user = user
        student.cover_image = req.FILES.get("cover_image")
        student.admission_number = req.POST.get("admission_number")
        student.phone = req.POST.get("phone")
        student.address = req.POST.get("address")
        student.date_of_birth = req.POST.get("date_of_birth")
        student.gender = req.POST.get("gender")
        student.admission_date = req.POST.get("admission_date")
        student.schoolclass = SchoolClass.objects.get(id=req.POST.get('schoolclass'))
        student.section = Section.objects.get(id=req.POST.get('section'))
        student.parent_name = req.POST.get("parent_name")
        student.parent_phone = req.POST.get("parent_phone")
        student.save()
        return redirect('manage_students')
    return render(req, "students/insert.html", data)

def manage_students(req):
    data = {
        "students" : Student.objects.all()
    }
    return render(req, "students/manage.html", data)


def student_details(req, id):
    data = {
        "student" : Student.objects.get(id=id)
    }
    return render(req, "students/details.html", data)

def edit_student(req, id):
    data = {
        "student" : Student.objects.get(id=id)
    }
    if req.method == "POST":
        student = Student.objects.get(id=id)
        student.user.first_name = req.POST.get('first_name')
        student.user.last_name = req.POST.get('last_name')
        student.user.username = req.POST.get('username')
        student.user.email = req.POST.get('email')
        student.user.save()

        student.cover_image = req.FILES.get('cover_image')
        student.admission_number = req.POST.get('admission_number')
        student.phone = req.POST.get('phone')
        student.address = req.POST.get('address')
        student.date_of_birth = req.POST.get('date_of_birth')
        student.gender = req.POST.get('gender')
        student.admission_date = req.POST.get('admission_date')
        student.parent_name = req.POST.get('parent_name')
        student.parent_phone = req.POST.get('parent_phone')
        student.save()
        return redirect('manage_students')
    return render(req, "students/insert.html", data)

def delete_student(req, id):
    data = {}
    try : 
        student = Student.objects.get(id=id)
        student.delete()
        return redirect(manage_students)
    except Student.DoesNotExist:
        data ['error'] = "This student does not exit"
    return redirect(manage_students)

def student_dashboard(req):
    return render(req, "students/dashboard.html")