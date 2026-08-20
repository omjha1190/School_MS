from django.shortcuts import render, redirect
from .models import StudentAttendance, TeacherAttendance
from academics.models import SchoolClass, Section
from students.models import Student

# Create your views here.
def student_attendance(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        schoolclass = req.POST.get('schoolclass')
        section = req.POST.get('section')
        date = req.POST.get('date')
    return render(req, "attendance/student_attendance.html", data)