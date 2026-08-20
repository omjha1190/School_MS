from django.shortcuts import render,redirect
from academics.models import SchoolClass,Section, Subject
from .models import Exam, Result
from students.models import Student

# Create your views here.
def insert_exam(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all()
    }
    if req.method == "POST":
        exam = Exam()
        exam.name = req.POST.get('name')
        exam.date = req.POST.get('date')
        exam.save()
        exam.schoolclass.set(req.POST.getlist('schoolclasses'))
        return redirect("manage_exams")
    return render(req, "examinations/insert_exam.html", data)

def manage_exams(req):
    data = {
        "exams" : Exam.objects.all()
    }
    return render(req, "examinations/manage_exams.html", data)

def edit_exam(req, id):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "exam" : Exam.objects.get(id=id)
    }
    if req.method == "POST":
        exam = Exam.objects.get(id=id)
        exam.name = req.POST.get('name')
        exam.date = req.POST.get('date')
        exam.save()
        exam.schoolclass.set(req.POST.getlist('schoolclasses'))
        return redirect("manage_exams")
    return render(req, "examinations/insert_exam.html", data)


def delete_exam(req, id):
    data = {}
    try :
        exam = Exam.objects.get(id=id)
        exam.delete()
        return redirect("manage_exams")
    except exam.DoesNotExist:
        data ['error'] = "This exam is not available"
    return redirect("manage_exams")

def insert_result(req):
    data = {
        "students" : Student.objects.all(),
        "exams" : Exam.objects.all(),
        "subjects" : Subject.objects.all()
    }
    if req.method == "POST":
        result = Result()
        result.student = Student.objects.get(id=req.POST.get('student'))
        result.exam = Exam.objects.get(id=req.POST.get('exam'))
        result.subject = Subject.objects.get(id=req.POST.get('subject'))
        result.marks = req.POST.get('marks')
        result.save()
        return redirect("manage_results")
    return render(req, "examinations/insert_result.html", data)

def manage_results(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "sections": Section.objects.values_list("name", flat=True).distinct(),
    }
    if req.method == "GET":
        schoolclass = req.GET.get('schoolclass')
        section = req.GET.get('section')

        if schoolclass and section:
            students = Student.objects.filter(schoolclass=schoolclass, section__name=section)

            data ['students'] = students
            data ['selected_class'] = schoolclass
            data ['selected_section'] = section
    return render(req, "examinations/manage_results.html", data)