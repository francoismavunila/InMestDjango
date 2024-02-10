from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name","course_description","course_date_created","course_date_modified")
# Register your models here.
admin.site.register(Course,CourseAdmin)