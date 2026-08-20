from django.urls import path
from students import views

urlpatterns = [
    path('insert/', views.insert_student, name="insert_student"),
    path('manage/', views.manage_students, name="manage_students"),
    path('details/<int:id>/', views.student_details, name="student_details"),
    path('edit/<int:id>/', views.edit_student, name="edit_student"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
    path('dashboard/', views.student_dashboard, name="student_dashboard"),
]
