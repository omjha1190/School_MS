from django.urls import path
from examinations import views

urlpatterns = [
    path('insert/exam/', views.insert_exam, name="insert_exam"),
    path('manage/exam/', views.manage_exams, name="manage_exams"),
    path('edit/exam/<int:id>/', views.edit_exam, name="edit_exam"),
    path('delete/exam/<int:id>/', views.delete_exam, name="delete_exam"),
    path('insert/result/', views.insert_result, name="insert_result"),
    path('manage/results/', views.manage_results, name="manage_results"),
]
