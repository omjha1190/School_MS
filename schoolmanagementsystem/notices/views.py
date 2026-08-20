from django.shortcuts import render, redirect
from .models import Notice
# Create your views here.

def insert_notice(req):
    if req.method == "POST":
        notice = Notice()
        notice.title = req.POST.get('title')
        notice.description = req.POST.get('description')
        notice.created_by = req.user
        notice.date = req.POST.get('date')
        notice.save()
        return redirect(manage_notices)
    return render(req, "notices/insert.html")

def manage_notices(req):
    data = {
        "notices" : Notice.objects.all(),
    }
    return render(req, "notices/manage.html", data)

def edit_notice(req, id):
    data = {
        "notice" : Notice.objects.get(id=id)
    }
    if req.method == "POST":
        notice = Notice.objects.get(id=id)
        notice.title = req.POST.get('title')
        notice.description = req.POST.get('description')
        notice.date = req.POST.get('date')
        notice.save()
        return redirect(manage_notices)
    return render(req, "notices/insert.html", data)

def delete_notice(req, id):
    data = {}
    try :
        notice = Notice.objects.get(id=id)
        notice.delete()
        return redirect(manage_notices)
    except Notice.DoesNotExist:
        data ['error'] = "This Notice is not available"
    return redirect(manage_notices)    