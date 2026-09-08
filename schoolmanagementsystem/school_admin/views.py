from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def admin_dashboard(req):
    if req.user.userprofile.role != "admin":
        return redirect("home")
    return render(req, "school_admin/dashboard.html")