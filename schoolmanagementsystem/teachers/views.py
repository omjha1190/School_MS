from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .models import Teacher


# Create your views here.
def insert_teacher(req):
    if req.method == 'POST':
        user = User()
        user.first_name = req.POST.get('first_name')
        user.last_name = req.POST.get('last_name')
        user.username = req.POST.get('username')
        user.email = req.POST.get('email')
        user.password = req.POST.get('password')
        user.confirm_password = req.POST.get('confirm_password')
        if user.password != user.confirm_password:
            return render(req, "teachers/insert.html", {
                'error': 'Passwords do not match'
            })
        user.set_password(user.password)
        user.save()

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.role = 'teacher'
        user_profile.save()

        teacher = Teacher()
        teacher.user = user
        teacher.phone = req.POST.get('phone')
        teacher.address = req.POST.get('address')
        teacher.qualification = req.POST.get('qualification')
        teacher.joining_date = req.POST.get('joining_date')
        teacher.gender = req.POST.get('gender')
        teacher.cover_image = req.FILES.get('cover_image')
        teacher.is_class_teacher = req.POST.get('is_class_teacher') == 'on'
        teacher.save()
        return redirect('manage_teachers')
    return render(req, "teachers/insert.html")


def manage_teachers(req):
    data = {
        "teachers" : Teacher.objects.all()
    }
    return render(req, "teachers/manage.html", data)

def teacher_details(req, id):
    data = {
        "teacher" : Teacher.objects.get(id=id)
    }
    return render(req, "teachers/details.html", data)

def edit_teacher(req, id):
    data = {
        "teacher" : Teacher.objects.get(id=id)
    }
    if req.method == "POST":
        teacher = Teacher.objects.get(id=id)
        teacher.user.first_name = req.POST.get("first_name")
        teacher.user.last_name = req.POST.get("last_name")
        teacher.user.username = req.POST.get("username")
        teacher.user.email = req.POST.get("email")
        teacher.user.save()

        teacher.phone = req.POST.get("phone")
        teacher.address = req.POST.get("address")
        teacher.qualification = req.POST.get("qualification")
        teacher.joining_date = req.POST.get("joining_date")
        teacher.gender = req.POST.get("gender")
        teacher.cover_image = req.FILES.get("cover_image")
        teacher.is_class_teacher = req.POST.get("is_class_teacher") == 'on'
        teacher.save()
        return redirect('manage_teachers')
    return render(req, "teachers/insert.html", data)

def delete_teacher(req, id):
    data = {}
    try:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return redirect(manage_teachers)
    except Teacher.DoesNotExist:
        data ['error'] = "This teacher does not exit"
    return redirect(manage_teachers)    


def teacher_dashboard(req):
    return render(req, "teachers/dashboard.html")