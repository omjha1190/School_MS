from django.urls import path
from attendance import views

urlpatterns = [
    path('student/', views.student_attendance, name="student_attendance")
]
