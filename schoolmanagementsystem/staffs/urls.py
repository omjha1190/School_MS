from django.urls import path
from staffs import views

urlpatterns = [
    path("insert/", views.insert_staff, name="insert_staff"),
    path("manage/", views.manage_staffs, name="manage_staffs"),
]
