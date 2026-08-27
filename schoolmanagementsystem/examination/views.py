from django.shortcuts import render, redirect
from academics.models import SchoolClass, Section, Subject
from students.models import Student
from .models import Exam, ExamSchedule, Result

# Create your views here.
def insert_exam(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "exam_modes" : Exam.EXAM_MODE,
        "exam_status" : Exam.EXAM_STATUS
    }
    if req.method == "POST":
        exam = Exam()
        exam.exam_name = req.POST.get('exam_name')
        exam.academic_year = req.POST.get('academic_year')
        exam.mode = req.POST.get('mode')
        exam.start_date = req.POST.get('start_date')
        exam.end_date = req.POST.get('end_date')
        exam.status = req.POST.get('status')
        exam.instructions = req.POST.get('instructions')
        exam.description = req.POST.get('description')
        exam.save()
        exam.schoolclass.set(req.POST.getlist('schoolclasses'))
        return redirect("manage_exams")
    return render(req, "examination/insert_exam.html", data)

def manage_exams(req):
    data = {
        "exams" : Exam.objects.all(),
    }
    return render(req, "examination/manage_exams.html", data)

def view_exam(req, id):
    data = {
        "exam" : Exam.objects.get(id=id)
    }
    return render(req, "examination/view_exam.html", data)

def edit_exam(req, id):
    data = {
        "exam" : Exam.objects.get(id=id),
        "schoolclasses" : SchoolClass.objects.all(),
        "exam_modes" : Exam.EXAM_MODE,
        "exam_status" : Exam.EXAM_STATUS
    }
    if req.method == "POST":
        exam = Exam.objects.get(id=id)
        exam.exam_name =req.POST.get("exam_name")
        exam.academic_year =req.POST.get("academic_year")
        exam.mode =req.POST.get("mode")
        exam.start_date =req.POST.get("start_date")
        exam.end_date =req.POST.get("end_date")
        exam.status =req.POST.get("status")
        exam.instructions =req.POST.get("instructions")
        exam.description =req.POST.get("description")
        exam.save()
        exam.schoolclass.set(req.POST.getlist('schoolclasses'))
        return redirect("manage_exams")
    return render(req, "examination/insert_exam.html", data)

def delete_exam(req, id):
    data = {}
    try:
        exam = Exam.objects.get(id=id)
        exam.delete()
        return redirect("manage_exams")
    except Exam.DoesNotExist:
        data ['error'] = "This exam is not available"
    return redirect("manage_exams")
