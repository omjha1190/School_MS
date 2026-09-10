from django.urls import path
from students import views

urlpatterns = [
    path('insert/', views.insert_student, name="insert_student"),
    path('manage/', views.manage_students, name="manage_students"),
    path('details/<int:id>/', views.student_details, name="student_details"),
    path('edit/<int:id>/', views.edit_student, name="edit_student"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
    path('dashboard/', views.student_dashboard, name="student_dashboard"),
    path('profile/', views.student_profile, name="student_profile"),
    path('class/', views.student_class, name="student_class"),
    path('subjects/', views.student_subjects, name="student_subjects"),
    path('attendance/', views.student_attendances, name="student_attendances"),
    path('timetable/', views.student_timetable, name="student_timetable"),
]
