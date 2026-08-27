from django.urls import path
from examination import views

urlpatterns = [
    path("insert/exam/", views.insert_exam, name="insert_exam"),
    path("manage/exam/", views.manage_exams, name="manage_exams"),
    path("exam/details/<int:id>/", views.view_exam, name="view_exam"),
    path("edit/exam/<int:id>/", views.edit_exam, name="edit_exam"),
    path("delete/exam/<int:id>/", views.delete_exam, name="delete_exam"),
    path("insert/examschedule/", views.insert_examschedule, name="insert_examschedule"),
    path("manage/examschedule/", views.manage_examschedules, name="manage_examschedules"),
    path("edit/examschedule/<int:id>/", views.edit_examschedule, name="edit_examschedule"),
    path("delete/examschedule/<int:id>/", views.delete_examschedule, name="delete_examschedule"),
]
