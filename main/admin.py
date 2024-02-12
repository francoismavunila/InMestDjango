from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name","course_description","course_date_created","course_date_modified")

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("class_schedule", "attendee", "is_present", "date_created", "date_modified", "author")
    
class QueryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "submitted_by", "assigned_to" , "resolution_status", "date_created", "date_modified", "author" )
    
class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ("query", "comment", "date_created", "date_modified", "author")
    
# Register your models here.
admin.site.register(Course,CourseAdmin)
admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance, AttendanceAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(QueryComment, QueryCommentAdmin)