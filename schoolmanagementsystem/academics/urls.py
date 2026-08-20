from django.urls import path
from academics import views

urlpatterns = [
    path('insert/class/', views.insert_class, name="insert_class"),
    path('manage/class/', views.manage_classes, name="manage_classes"),
    path('edit/class/<int:id>/', views.edit_class, name="edit_class"),
    path('delete/class/<int:id>/', views.delete_class, name="delete_class"),
    path('insert/section/', views.insert_section, name="insert_section"),
    path('insert/subject/', views.insert_subject, name="insert_subject"),
    path('insert/teacher/assignment/', views.insert_teacher_assignment, name="insert_teacher_assignment"),
    path('manage/teacher/assignment/', views.manage_teacher_assignment, name="manage_teacher_assignment"),
    path('delete/teacher/assignment/<int:id>/', views.delete_teacher_assignment, name="delete_teacher_assignment"),
]
