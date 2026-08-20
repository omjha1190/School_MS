from django.urls import path
from teachers import views

urlpatterns = [
    path("insert/teacher/", views.insert_teacher, name="insert_teacher"),
    path("manage/teachers/", views.manage_teachers, name="manage_teachers"),
    path("teachers/details/<int:id>/", views.teacher_details, name="teacher_details"),
    path("edit/teachers/<int:id>/", views.edit_teacher, name="edit_teacher"),
    path("delete/teacher/<int:id>/", views.delete_teacher, name="delete_teacher"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard")
]
