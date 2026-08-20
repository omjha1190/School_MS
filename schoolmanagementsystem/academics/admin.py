from django.contrib import admin
from .models import SchoolClass, Section, Subject, TeacherAssignment

# Register your models here.
admin.site.register(SchoolClass)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(TeacherAssignment)