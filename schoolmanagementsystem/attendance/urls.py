from django.urls import path
from attendance import views

urlpatterns = [
    path('student/insert/', views.student_attendance, name="student_attendance"),
    path('student/manage/<int:section_id>/', views.manage_student_attendance, name="manage_student_attendance"),
]
