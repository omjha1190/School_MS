from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .models import Student
from academics.models import SchoolClass, Section, StudentEnrollment, TeacherAssignment ,ClassTeacher, Timetable
from django.contrib.auth.decorators import login_required
from attendance.models import StudentAttendance
from fees.models import Fee


# Create your views here.
@login_required
def student_dashboard(req):
    if req.user.userprofile.role != "student":
        return redirect("home")
    student = req.user.student
    enrollment = student.enrollments.first()

    present_count = StudentAttendance.objects.filter(enrollment=enrollment, status=True).count()
    absent_count = StudentAttendance.objects.filter(enrollment=enrollment, status=False).count()

    total_fee_count = Fee.objects.filter(student=student).count()
    paid_fee_count = Fee.objects.filter(student=student, status="Paid").count()
    pending_fee_count = Fee.objects.filter(student=student, status="Pending").count()
    overdue_fee_count = Fee.objects.filter(student=student, status="Overdue").count()

    data = {
        "student" : student,
        "enrollment" : enrollment,
        "present_count" : present_count,
        "absent_count" : absent_count,
        "total_attendance" : present_count + absent_count,
        "total_fee_count" : total_fee_count,
        "paid_fee_count" : paid_fee_count,
        "pending_fee_count" : pending_fee_count,
        "overdue_fee_count" : overdue_fee_count,
    }
    return render(req, "students/dashboard.html", data)

def insert_student(req):
    data = {
        "schoolclasses" : SchoolClass.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        user = User()
        user.first_name = req.POST.get("first_name")
        user.last_name = req.POST.get("last_name")
        user.username = req.POST.get("username")
        user.email = req.POST.get("email")
        user.password = req.POST.get("password")
        user.confirm_password = req.POST.get("confirm_password")
        if user.password != user.confirm_password:
            data["error"] = "Password do not match"
            return render(req, "students/insert.html", data)
        user.set_password(user.password)
        user.save()

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.role = "student"
        user_profile.save()

        student = Student()
        student.user = user
        student.cover_image = req.FILES.get("cover_image")
        student.admission_number = req.POST.get("admission_number")
        student.phone = req.POST.get("phone")
        student.address = req.POST.get("address")
        student.date_of_birth = req.POST.get("date_of_birth")
        student.gender = req.POST.get("gender")
        student.admission_date = req.POST.get("admission_date")
        student.parent_name = req.POST.get("parent_name")
        student.parent_phone = req.POST.get("parent_phone")
        student.save()

        StudentEnrollment.objects.create(
            student=student,
            section_id=req.POST.get("section"),
            academic_year=req.POST.get("academic_year"),
            roll_no=req.POST.get("roll_no"),
        )

        return redirect('manage_students')
    return render(req, "students/insert.html", data)

def manage_students(req):
    data = {
        "students" : Student.objects.all()
    }
    return render(req, "students/manage.html", data)


def student_details(req, id):
    data = {
        "student" : Student.objects.get(id=id)
    }
    return render(req, "students/details.html", data)

def edit_student(req, id):
    data = {
        "student" : Student.objects.get(id=id),
        "schoolclasses" : SchoolClass.objects.all(),
        "sections" : Section.objects.all(),
    }
    if req.method == "POST":
        student = Student.objects.get(id=id)
        student.user.first_name = req.POST.get('first_name')
        student.user.last_name = req.POST.get('last_name')
        student.user.username = req.POST.get('username')
        student.user.email = req.POST.get('email')
        student.user.save()

        student.cover_image = req.FILES.get('cover_image')
        student.admission_number = req.POST.get('admission_number')
        student.phone = req.POST.get('phone')
        student.address = req.POST.get('address')
        student.date_of_birth = req.POST.get('date_of_birth')
        student.gender = req.POST.get('gender')
        student.admission_date = req.POST.get('admission_date')
        student.parent_name = req.POST.get('parent_name')
        student.parent_phone = req.POST.get('parent_phone')
        student.save()

        enrollment = student.enrollments.first()

        if enrollment:
            enrollment.section_id = req.POST.get("section")
            enrollment.academic_year = req.POST.get("academic_year")
            enrollment.roll_no = req.POST.get("roll_no")
            enrollment.save()
        else:
            StudentEnrollment.objects.create(
                student=student,
                section_id=req.POST.get("section"),
                academic_year=req.POST.get("academic_year"),
                roll_no=req.POST.get("roll_no"),
            )
        return redirect('manage_students')
    return render(req, "students/insert.html", data)

def delete_student(req, id):
    data = {}
    try : 
        student = Student.objects.get(id=id)
        student.delete()
        return redirect(manage_students)
    except Student.DoesNotExist:
        data ['error'] = "This student does not exit"
    return redirect(manage_students)


def student_profile(req):
    if req.user.userprofile.role != "student":
        return redirect("home")
    student = req.user.student
    data = {
        "student" : student
    }
    return render(req, "students/profile.html", data)

def student_class(req):
    if req.user.userprofile.role != "student":
        return redirect("home")

    student = req.user.student
    enrollment = student.enrollments.first()

    class_teacher = ClassTeacher.objects.filter(section=enrollment.section, academic_year=enrollment.academic_year).first()
    subject_teachers = TeacherAssignment.objects.filter(section=enrollment.section).select_related("teacher__user", "subject")

    data = {
        "student" : student,
        "enrollment" : enrollment,
        "class_teacher" : class_teacher,
        "subject_teachers" : subject_teachers
    }
    return render(req, "students/class.html", data)

def student_subjects(req):
    if req.user.userprofile.role != "student":
        return redirect("home")

    student = req.user.student
    enrollment = student.enrollments.first()

    subject_teachers = TeacherAssignment.objects.filter(section=enrollment.section).select_related("teacher__user", "subject")

    data = {
        "student" : student,
        "enrollment" : enrollment,
        "subject_teachers" : subject_teachers
    }
    return render(req, "students/subjects.html", data)

def student_attendances(req):
    if req.user.userprofile.role != "student":
        return redirect("home")

    student = req.user.student
    enrollment = student.enrollments.first()

    attendance = StudentAttendance.objects.filter(enrollment=enrollment).order_by("-date")
    total_days = attendance.count()
    present_days = attendance.filter(status=True).count()
    absent_days = attendance.filter(status=False).count()

    if total_days > 0:
        present_percentage = round(
            (present_days / total_days) * 100, 2
        )
    else : 
        present_days = 0
    data = {
        "student" : student,
        "enrollment" : enrollment,
        "attendance" : attendance,
        "total_days" : total_days,
        "present_days" : present_days,
        "absent_days" : absent_days,
        "present_percentage" : present_percentage
    }
    return render(req, "students/attendance.html", data)

def student_timetable(req):
    if req.user.userprofile.role != "student":
        return redirect("home")
    student = req.user.student
    enrollment = student.enrollments.first()

    timetables = Timetable.objects.filter(section=enrollment.section, academic_year=enrollment.academic_year).prefetch_related("subjects")

    data = {
        "student" : student,
        "enrollment" : enrollment,
        "timetables" : timetables
    }
    return render(req, "students/timetable.html",data)