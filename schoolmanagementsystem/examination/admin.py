from django.contrib import admin
from .models import Exam, ExamSchedule, Result

# Register your models here.
admin.site.register(Exam)
admin.site.register(ExamSchedule)
admin.site.register(Result)