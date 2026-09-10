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
    path('edit/teacher/assignment/<int:id>/', views.edit_teacher_assignment, name="edit_teacher_assignment"),
    path('delete/teacher/assignment/<int:id>/', views.delete_teacher_assignment, name="delete_teacher_assignment"),
    path("insert/enrollment/", views.insert_enrollment, name="insert_enrollment"),
    path("manage/enrollment/", views.manage_enrollments, name="manage_enrollments"),
    path("edit/enrollment/<int:id>/", views.edit_enrollment, name="edit_enrollment"),
    path("delete/enrollment/<int:id>/", views.delete_enrollment, name="delete_enrollment"),
    path('insert/class/teacher/', views.insert_class_teacher, name="insert_class_teacher"),
    path('manage/class/teacher/', views.manage_class_teachers, name="manage_class_teachers"),
    path('edit/class/teacher/<int:id>/', views.edit_class_teacher, name="edit_class_teacher"),
    path('delete/class/teacher/<int:id>/', views.delete_class_teacher, name="delete_class_teacher"),
    path("insert/timetable/", views.insert_timetable, name="insert_timetable"),
    path("manage/timetable/", views.manage_timetable, name="manage_timetable"),
    path("edit/timetable/<int:id>/", views.edit_timetable, name="edit_timetable"),
    path("delete/timetable/<int:id>/", views.delete_timetable, name="delete_timetable"),
]
