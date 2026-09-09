from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from students.models import Student
from teachers.models import Teacher
from staffs.models import Staff
from academics.models import SchoolClass, Section
from library.models import Book
from fees.models import Fee
from notices.models import Notice
from attendance.models import StudentAttendance, TeacherAttendance


# Create your views here.
@login_required
def admin_dashboard(req):
    if req.user.userprofile.role != "admin":
        return redirect("home")

    today = timezone.localdate()

    data = {
        "student_count" : Student.objects.count(),
        "teacher_count" : Teacher.objects.count(),
        "staff_count" : Staff.objects.count(),
        "class_count" : SchoolClass.objects.count(),
        "section_count" : Section.objects.count(),
        "book_count" : Book.objects.count(),
        "pending_fee_count" : Fee.objects.filter(status="Pending").count(),
        "paid_fee_count": Fee.objects.filter(status="Paid").count(),
        "overdue_fee_count": Fee.objects.filter(status="Overdue").count(),
        "recent_notices": Notice.objects.order_by("-date")[:5],
        "student_present_today" : StudentAttendance.objects.filter(date=today, status=True).count(),
        "student_absent_today" : StudentAttendance.objects.filter(date=today, status=False).count(),
        "teacher_present_today" : TeacherAttendance.objects.filter(date=today, status=True).count(),
        "teacher_absent_today" : TeacherAttendance.objects.filter(date=today, status=False).count(),
    }
    return render(req, "school_admin/dashboard.html", data)