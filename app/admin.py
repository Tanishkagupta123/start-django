from django.contrib import admin
from .models import Student,Aadhar,Department,Employee

# Register your models here.

admin.site.register(Student)
admin.site.register(Aadhar)
admin.site.register(Department)

admin.site.register(Employee)

