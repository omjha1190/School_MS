from django.urls import path
from teachers import views

urlpatterns = [
    path("insert/", views.insert_teacher, name="insert_teacher"),
    path("manage/teachers/", views.manage_teachers, name="manage_teachers"),
    path("teachers/details/<int:id>/", views.teacher_details, name="teacher_details"),
    path("edit/teachers/<int:id>/", views.edit_teacher, name="edit_teacher"),
    path("delete/teacher/<int:id>/", views.delete_teacher, name="delete_teacher"),
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("classes/", views.teacher_classes, name="teacher_classes"),
    path("subjets/", views.teacher_subjects, name="teacher_subjects"),
    path("students/", views.teacher_students, name="teacher_students"),
    path("attendance/", views.my_attendance, name="my_attendance"),
    path("assignments/", views.teacher_assignments, name="teacher_assignments"),
    path("submissions/", views.teacher_submissions, name="teacher_submissions"),
    path("marks/", views.teacher_marks, name="teacher_marks"),
    path("enter/marks/<int:id>/", views.enter_marks, name="enter_marks"),
    path("timetable/", views.teacher_timetable, name="teacher_timetable"),
    path("notices/", views.teacher_notices, name="teacher_notices"),
    path("profile/", views.teacher_profile, name="teacher_profile"),
]
