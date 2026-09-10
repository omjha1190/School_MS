from django.contrib import admin
from .models import SchoolClass, Section, Subject, TeacherAssignment, StudentEnrollment, ClassTeacher, Timetable

# Register your models here.
admin.site.register(SchoolClass)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(TeacherAssignment)
admin.site.register(StudentEnrollment)
admin.site.register(ClassTeacher)
admin.site.register(Timetable)