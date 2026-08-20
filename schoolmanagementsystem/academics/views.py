from django.shortcuts import render, redirect
from .models import SchoolClass, Section, Subject, TeacherAssignment
from teachers.models import Teacher

# Create your views here.
def insert_class(req):
    if req.method == "POST":
        schoolclass = SchoolClass()
        schoolclass.name = req.POST.get('name')
        schoolclass.save()
        return redirect('manage_classes')
    return render(req, "academics/insert_class.html")

def manage_classes(req):
    data = {
        "schoolclass" : SchoolClass.objects.all(),
        "section" : Section.objects.all(),
        "subjects" : Subject.objects.all(),
    }
    return render(req, "academics/manage_class.html", data)

def edit_class(req, id):
    data = {
        "schoolclass" : SchoolClass.objects.get(id=id)
    }
    if req.method == "POST":
        schoolclass = SchoolClass.objects.get(id=id)
        schoolclass.name = req.POST.get('name')
        schoolclass.save()
        return redirect('manage_classes')
    return render(req, "academics/insert_class.html", data)

def delete_class(req, id):
    data = {}
    try:
        schoolclass = SchoolClass.objects.get(id=id)
        schoolclass.delete()
        return redirect(manage_classes)
    except SchoolClass.DoesNotExist:
        data ['error'] = "This class does not exit"
    return redirect('manage_classes') 

def insert_section(req):
    data = {
        "schoolclass" : SchoolClass.objects.all(),
    }
    if req.method == "POST":
        section = Section()
        section.name = req.POST.get('name')
        section.schoolclass = SchoolClass.objects.get(id=req.POST.get("schoolclass"))
        section.save()
        return redirect(manage_classes)
    return render(req, "academics/insert_section.html", data)   

def insert_subject(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
    }
    if req.method == "POST":
        subject = Subject()
        subject.name = req.POST.get('name')
        subject.save()
        subject.schoolclasses.set(req.POST.getlist('schoolclasses'))
        return redirect(manage_classes)
    return render(req, "academics/insert_subject.html", data) 

def insert_teacher_assignment(req):
    data = {
        "teachers" : Teacher.objects.all(),
        "subjects" : Subject.objects.all(),
        "schoolclasses" : SchoolClass.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        teacherassignment = TeacherAssignment()
        teacherassignment.teacher = Teacher.objects.get(id=req.POST.get('teacher'))
        teacherassignment.subject = Subject.objects.get(id=req.POST.get('subject'))
        teacherassignment.schoolclass = SchoolClass.objects.get(id=req.POST.get('schoolclass'))
        teacherassignment.section = Section.objects.get(id=req.POST.get('section'))
        teacherassignment.save()
        return redirect('manage_teacher_assignment')
    return render(req, "academics/insert_teacher_assignment.html", data)

def manage_teacher_assignment(req): 
    data = {
        "teacherassignments" : TeacherAssignment.objects.all()
    }
    return render(req, "academics/manage_teacher_assignment.html", data)

def edit_teacher_assignment(req, id):
    data = {
        ""
    }
    return render(req, "academics/insert_teacher_assignment.html")

def delete_teacher_assignment(req, id):
    data = {}
    try:
        teacherassignment = TeacherAssignment.objects.get(id=id)
        teacherassignment.delete()
        return redirect(manage_teacher_assignment)
    except TeacherAssignment.DoesNotExist:
        data ['error'] = "No teacher is assigned to it"
    return redirect('manage_teacher_assignment')    
