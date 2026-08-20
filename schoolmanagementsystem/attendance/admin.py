from django.contrib import admin
from .models import StudentAttendance, TeacherAttendance

# Register your models here.
admin.site.register(StudentAttendance)
admin.site.register(TeacherAttendance)