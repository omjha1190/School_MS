from django.urls import path
from assignments import views

urlpatterns = [
   path("insert/", views.insert_assignment, name="insert_assignment"),
   path("manage/", views.manage_assignments, name="manage_assignments"),
   path("details/<int:id>/", views.assignment_details, name="assignment_details"),
   path("edit/<int:id>/", views.edit_assignment, name="edit_assignment"),
   path("delete/<int:id>/", views.delete_assignment, name="delete_assignment"),
]
