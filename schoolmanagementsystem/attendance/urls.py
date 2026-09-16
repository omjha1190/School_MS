from django.urls import path
from attendance import views

urlpatterns = [
    path('student/insert/', views.student_attendance, name="student_attendance"),
    path('manage/student-attendance/<int:section_id>/', views.manage_student_attendance, name="manage_student_attendance"),
    path('teacher/insert/', views.teacher_attendance, name="teacher_attendance"),
    path('manage/teacher-attendance/', views.manage_teacher_attendance, name="manage_teacher_attendance"),
    path('dashboard/', views.attendance_dashboard, name="attendance_dashboard"),
]
