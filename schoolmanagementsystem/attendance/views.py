from django.shortcuts import render, redirect
from .models import StudentAttendance, TeacherAttendance
from academics.models import SchoolClass, Section, StudentEnrollment
from students.models import Student
from django.db.models import Prefetch
from teachers.models import Teacher

# Create your views here.
def student_attendance(req):
    data = {
        "schoolclasses": SchoolClass.objects.all(),
        "sections": Section.objects.all(),
    }

    if req.method == "POST":

        action = req.POST.get("action")
        section_id = req.POST.get("section")
        date = req.POST.get("date")

        if action == "load":

            data["selected_class"] = req.POST.get("schoolclass")
            data["selected_section"] = section_id
            data["selected_date"] = date
            data["enrollments"] = StudentEnrollment.objects.filter(section_id=section_id)

        elif action == "save":
            absent_students = req.POST.getlist("absent_students")
            enrollments = StudentEnrollment.objects.filter(section_id=section_id)

            for enrollment in enrollments:

                if str(enrollment.id) in absent_students:
                    status = False
                else:
                    status = True

                StudentAttendance.objects.update_or_create(enrollment=enrollment,date=date,defaults={"status": status})

            return redirect("manage_student_attendance", section_id=section_id)
    return render(req, "attendance/insert_student_attendance.html", data)

def manage_student_attendance(req, section_id):
    data = {
        "schoolclasses": SchoolClass.objects.all(),
        "sections": Section.objects.all(),
    }

    if req.method == "POST":

        schoolclass_id = req.POST.get("schoolclass")
        section_id = req.POST.get("section")
        date = req.POST.get("date")

        data["selected_class"] = schoolclass_id
        data["selected_section"] = section_id
        data["selected_date"] = date

        data["attendances"] = StudentAttendance.objects.filter( enrollment__section_id=section_id, date=date ).select_related( "enrollment__student", "enrollment__section__schoolclass" ).order_by( "enrollment__roll_no" )
    return render(req, "attendance/manage_student_attendance.html", data)


def teacher_attendance(req):
    data = {
        "teachers": Teacher.objects.all()
    }
    if req.method == "POST":
        action = req.POST.get("action")
        date = req.POST.get("date")
        if action == "load":
            data["selected_date"] = date
        elif action == "save":
            absent_teachers = req.POST.getlist("absent_teachers")
            teachers = Teacher.objects.all()
            for teacher in teachers:
                if str(teacher.id) in absent_teachers:
                    status = False
                else:
                    status = True
                TeacherAttendance.objects.update_or_create( teacher=teacher, date=date, defaults={ "status": status } )
            return redirect("manage_teacher_attendance")

    return render(req,"attendance/insert_teacher_attendance.html", data)


def manage_teacher_attendance(req):
    data = {}
    if req.method == "POST":
        date = req.POST.get("date")
        data["selected_date"] = date
        data["attendances"] = TeacherAttendance.objects.filter(date=date).select_related("teacher").order_by("teacher")
    return render(req,"attendance/manage_teacher_attendance.html",data)