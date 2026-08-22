from django.urls import path
from fees import views

urlpatterns = [
    path("insert/", views.insert_fee, name="insert_fee"),
    path("manage/", views.manage_fees, name="manage_fees"),
    path("edit/<int:id>/", views.edit_fee, name="edit_fee"),
    path("delete/<int:id>/", views.delete_fee, name="delete_fee"),
    path("history/<int:id>/", views.fees_history, name="fees_history"),
]
