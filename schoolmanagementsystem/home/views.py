from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login, logout as auth_logout
# Create your views here.

def home(req):
    return render(req, "home/home.html") 

def login(req):
    form = AuthenticationForm(req, data=req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            user = form.get_user()
            auth_login(req, user)

            if user.userprofile.role == "student":
                return redirect("student_dashboard")
            elif user.userprofile.role == "teacher":
                return redirect("teacher_dashboard")
            elif user.userprofile.role == "admin":
                return redirect("admin_dashboard")
            return redirect("home")
    data ={
        "loginForm" : form
    }
    return render(req, "home/login.html", data)

def logout(req):
    auth_logout(req)
    return redirect("home")
    