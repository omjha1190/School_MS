from django.shortcuts import render

# Create your views here.
def admin_dashboard(req):
    return render(req, "school_admin/dashboard.html")