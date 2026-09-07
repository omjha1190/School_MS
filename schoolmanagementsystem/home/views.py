from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login, logout as auth_logout
# Create your views here.

def home(req):
    return render(req, "home/home.html") 

def login(req):
    form = AuthenticationForm(req.POST or None)
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(req, user)
            return redirect("home")
    data ={
        "loginForm" : form
    }
    return render(req, "home/login.html", data)

def logout(req):
    auth_logout(req)
    return redirect("home")
    