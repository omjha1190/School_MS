from django.urls import path
from staffs import views

urlpatterns = [
    path("insert/", views.insert_staff, name="insert_staff"),
    path("manage/", views.manage_staffs, name="manage_staffs"),
    path("edit/<int:id>/", views.edit_staff, name="edit_staff"),
    path("delete/<int:id>/", views.delete_staff, name="delete_staff"),
]
