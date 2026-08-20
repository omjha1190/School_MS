from django.shortcuts import render, redirect
from .models import Assignment
from academics.models import Section, Subject
from teachers.models import Teacher

# Create your views here.
def insert_assignment(req):
    data = {
        "sections" : Section.objects.all(),
        "subjects" : Subject.objects.all(),
        "teachers" : Teacher.objects.all()
    }
    if req.method == "POST":
        assignment = Assignment()
        assignment.title = req.POST.get('title')
        assignment.description = req.POST.get('description')
        assignment.subject = Subject.objects.get(id=req.POST.get('subject'))
        assignment.teacher = Teacher.objects.get(id=req.POST.get('teacher'))
        assignment.class_section = Section.objects.get(id=req.POST.get('class_section'))
        assignment.assigned_date = req.POST.get('assigned_date')
        assignment.due_date = req.POST.get('due_date')
        assignment.save()
        return redirect("manage_assignments")
    return render(req, "assignments/insert_assignment.html", data)

def manage_assignments(req):
    data = {
        "assignments" : Assignment.objects.all(),
        "sections" : Section.objects.all()
    }
    if req.method == "GET":
        class_section = req.GET.get("class_section")

        if class_section:
            assignments = Assignment.objects.filter(class_section=class_section)

            data["assignments"] = assignments
            data["selected_section"] = class_section

    return render(req, "assignments/manage_assignments.html", data)

def edit_assignment(req, id):
    data = {
        "assignment" : Assignment.objects.get(id=id),
        "sections" : Section.objects.all(),
        "subjects" : Subject.objects.all(),
        "teachers" : Teacher.objects.all()
    }
    if req.method == "POST":
        assignment = Assignment.objects.get(id=id)
        assignment.title = req.POST.get('title')
        assignment.description = req.POST.get('description')
        assignment.subject = Subject.objects.get(id=req.POST.get('subject'))
        assignment.teacher = Teacher.objects.get(id=req.POST.get('teacher'))
        assignment.class_section = Section.objects.get(id=req.POST.get('class_section'))
        assignment.assigned_date = req.POST.get('assigned_date')
        assignment.due_date = req.POST.get('due_date')
        assignment.save()
        return redirect("manage_assignments")
    return render(req, "assignments/insert_assignment.html", data)

def assignment_details(req, id):
    data = {
        "assignment" : Assignment.objects.get(id=id)
    }
    return render(req, "assignments/details_assignment.html", data)

def delete_assignment(req, id):
    data = {}
    try :
        assignment = Assignment.objects.get(id=id)
        assignment.delete()
        return redirect("manage_assignments")
    except Assignment.DoesNotExist:
        data ['error'] = "This assignment is not available"
    return redirect("manage_assignments")