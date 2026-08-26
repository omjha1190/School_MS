from django.urls import path
from staffpayments import views

urlpatterns = [
    path("insert/", views.insert_staffpayment, name="insert_staffpayment"),
    path("manage/", views.manage_staffpayments, name="manage_staffpayments"),
    path("history/<int:id>/", views.staffpayment_history, name="staffpayment_history"),
    path("edit/<int:id>/", views.edit_staffpayment, name="edit_staffpayment"),
    path("delete/<int:id>/", views.delete_staffpayment, name="delete_staffpayment"),
]
