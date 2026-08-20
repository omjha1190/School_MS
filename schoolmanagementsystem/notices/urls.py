from django.urls import path
from notices import views

urlpatterns = [
    path('insert/', views.insert_notice, name="insert_notice"),
    path('manage/', views.manage_notices, name="manage_notices"),
    path('edit/<int:id>/', views.edit_notice, name="edit_notice"),
    path('delete/<int:id>/', views.delete_notice, name="delete_notice"),
]
