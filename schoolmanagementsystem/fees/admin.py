from django.contrib import admin
from students.models import Student
from .models import Fee, FeeItem

# Register your models here.
admin.site.register(Fee)
admin.site.register(FeeItem)