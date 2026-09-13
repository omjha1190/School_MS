from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .models import Teacher
from django.contrib.auth.decorators import login_required
from assignments.models import Assignment, AssignmentSubmisssion
from academics.models import TeacherAssignment, ClassTeacher, StudentEnrollment, Timetable, Subject
from attendance.models import TeacherAttendance
from examination.models import Exam, Result
from notices.models import Notice


# Create your views here.
def insert_teacher(req):
    data = {
        "subjects" : Subject.objects.all()
    }
    if req.method == 'POST':
        user = User()
        user.first_name = req.POST.get('first_name')
        user.last_name = req.POST.get('last_name')
        user.username = req.POST.get('username')
        user.email = req.POST.get('email')
        user.password = req.POST.get('password')
        user.confirm_password = req.POST.get('confirm_password')
        if user.password != user.confirm_password:
            return render(req, "teachers/insert.html", {
                'error': 'Passwords do not match'
            })
        user.set_password(user.password)
        user.save()

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.role = 'teacher'
        user_profile.save()

        teacher = Teacher()
        teacher.user = user
        teacher.subject_id = req.POST.get('subject')
        teacher.phone = req.POST.get('phone')
        teacher.address = req.POST.get('address')
        teacher.qualification = req.POST.get('qualification')
        teacher.joining_date = req.POST.get('joining_date')
        teacher.gender = req.POST.get('gender')
        teacher.cover_image = req.FILES.get('cover_image')
        teacher.is_class_teacher = req.POST.get('is_class_teacher') == 'on'
        teacher.save()
        return redirect('manage_teachers')
    return render(req, "teachers/insert.html", data)


def manage_teachers(req):
    data = {
        "teachers" : Teacher.objects.all()
    }
    return render(req, "teachers/manage.html", data)

def teacher_details(req, id):
    teacher = Teacher.objects.get(id=id)

    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject","schoolclass","section")

    data = {
        "teacher": teacher,
        "assignments": assignments
    }
    return render(req, "teachers/details.html", data)

def edit_teacher(req, id):
    data = {
        "teacher" : Teacher.objects.get(id=id)
    }
    if req.method == "POST":
        teacher = Teacher.objects.get(id=id)
        teacher.user.first_name = req.POST.get("first_name")
        teacher.user.last_name = req.POST.get("last_name")
        teacher.user.username = req.POST.get("username")
        teacher.user.email = req.POST.get("email")
        teacher.user.save()

        teacher.phone = req.POST.get("phone")
        teacher.address = req.POST.get("address")
        teacher.qualification = req.POST.get("qualification")
        teacher.joining_date = req.POST.get("joining_date")
        teacher.gender = req.POST.get("gender")
        teacher.cover_image = req.FILES.get("cover_image")
        teacher.is_class_teacher = req.POST.get("is_class_teacher") == 'on'
        teacher.save()
        return redirect('manage_teachers')
    return render(req, "teachers/insert.html", data)

def delete_teacher(req, id):
    data = {}
    try:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return redirect(manage_teachers)
    except Teacher.DoesNotExist:
        data ['error'] = "This teacher does not exit"
    return redirect(manage_teachers)    

@login_required
def teacher_dashboard(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")

    teacher = req.user.teacher

    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject", "section", "schoolclass")
    class_teachers = ClassTeacher.objects.filter(teacher=teacher).select_related("section")
    teacher_assignments = Assignment.objects.filter(teacher=teacher).order_by("-assigned_date")

    data = {
        "teacher" : teacher,
        "assignments" : assignments,
        "class_teachers" : class_teachers,
        "teacher_assignments" : teacher_assignments,
        "total_subjects" : assignments.values("subject").distinct().count(),
        "total_sections" : assignments.values("section").distinct().count(),
        "total_assignments" : teacher_assignments.count()
    }
    return render(req, "teachers/dashboard.html", data)

def teacher_classes(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject", "schoolclass", "section")
    class_teachers = ClassTeacher.objects.filter(teacher=teacher).select_related("section", "section__schoolclass")

    data = {
        "teacher" : teacher,
        "assignments" : assignments,
        "class_teachers" : class_teachers
    }
    return render(req, "teachers/classes.html",data)

def teacher_subjects(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject", "schoolclass", "section")
    data = {
        "teacher" : teacher,
        "assignments" : assignments
    }
    return render(req, "teachers/subjects.html", data)

def teacher_students(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")

    teacher = req.user.teacher

    assignments = TeacherAssignment.objects.filter(teacher=teacher)
    enrollments = StudentEnrollment.objects.filter(section__in=assignments.values_list("section", flat=True))

    data ={
        "teacher" : teacher,
        "enrollments" : enrollments
    }
    return render(req, "teachers/students.html", data)

def my_attendance(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher
    attendance = TeacherAttendance.objects.filter(teacher=teacher).order_by("-date")

    total_days = attendance.count()
    present_days = attendance.filter(status=True).count()
    absent_days = attendance.filter(status=False).count()

    if total_days > 0:
        present_percentage = round(
            (present_days / total_days) * 100, 2
        )
    else :
        present_percentage = 0

    data = {
        "teacher":teacher,
        "attendance" : attendance,
        "total_days" : total_days,
        "present_days" : present_days,
        "absent_days" : absent_days,
        "present_percentage" : present_percentage,
    }
    return render(req, "teachers/attendance.html", data)

def teacher_assignments(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    assignments = Assignment.objects.filter(teacher=teacher).order_by("-assigned_date")

    data = {
        "teacher" : teacher,
        "assignments" : assignments
    }
    return render(req, "teachers/assignments.html", data)

def teacher_submissions(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    submissions = AssignmentSubmisssion.objects.filter(assignment__teacher=teacher).order_by("-submitted_date")

    data = {
        "teacher" : teacher,
        "submissions" : submissions
    }
    return render(req, "teachers/submissions.html", data)

def teacher_marks(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject", "schoolclass", "section")
    data = {
        "teacher" : teacher,
        "assignments" : assignments
    }
    return render(req, "teachers/marks.html", data)

def enter_marks(req, id):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    assignment = TeacherAssignment.objects.get(teacher=teacher, id=id)
    enrollments = StudentEnrollment.objects.filter(section=assignment.section).select_related("student")
    exams = Exam.objects.filter(schoolclass=assignment.schoolclass)

    if req.method == "POST":

        exam = Exam.objects.get(
            id=req.POST.get("exam")
        )

        for enrollment in enrollments:

            marks = req.POST.get(
                f"marks_{enrollment.student.id}"
            )

            if marks:
                Result.objects.update_or_create(
                    student=enrollment.student,
                    exam=exam,
                    subject=assignment.subject,
                    defaults={
                        "marks": marks,
                        "grade": "",
                        "remarks": ""
                    }
                )

        return redirect("teacher_marks")


    data = {
        "teacher" : teacher,
        "assignment" : assignment,
        "enrollments" : enrollments,
        "exams" : exams
    }
    return render(req, "teachers/enter_marks.html", data)

def teacher_timetable(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")

    teacher = req.user.teacher
    assignments = TeacherAssignment.objects.filter(teacher=teacher).select_related("subject", "schoolclass", "section")
    sections = assignments.values_list("section", flat=True).distinct()

    timetables = Timetable.objects.filter(section__in=sections).prefetch_related("subjects").order_by("day")

    for timetable in timetables:
        timetable.teacher_subjects = timetable.subjects.filter(
            id__in=assignments.values_list("subject", flat=True)
        )
    data = {
        "teacher" : teacher,
        "assignments" : assignments,
        "timetables" :timetables
    }
    return render(req, "teachers/timetable.html", data)

def teacher_notices(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher=req.user.teacher
    notices = Notice.objects.all().order_by("-date")

    data = {
        "teacher" : teacher,
        "notices" : notices
    }
    return render(req, "teachers/notices.html", data)

def teacher_profile(req):
    if req.user.userprofile.role != "teacher":
        return redirect("home")
    teacher = req.user.teacher

    data = {
        "teacher" : teacher
    }
    return render(req, "teachers/profile.html", data)