from django.contrib import admin
from .models import System_user , Teacher, Student

# Register your models here.

admin.site.register(System_user)
admin.site.register(Teacher)
admin.site.register(Student)
