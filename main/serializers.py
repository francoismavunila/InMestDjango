from rest_framework import serializers

from users.serializers import *

class CourseSerialzer(serializers.Serializer):
    course_name = serializers.CharField(max_length=50)
    course_description = serializers.CharField(max_length = 500)
    
class ClassScheduleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 500)
    description = serializers.CharField(max_length = 1000)
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_active = serializers.BooleanField()
    organizer = serializers.CharField(max_length = 255)
    cohort = CohortSerializer()
    venue = serializers.CharField(max_length = 255)
    course = CourseSerialzer()
    facilitator = IMUser()

class ClassAttendanceSerializer(serializers.Serializer):
    class_schedule = ClassScheduleSerializer()
    attendee = UserSerializer()
    is_present = serializers.BooleanField()
    author = UserSerializer()

class QuerySerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 255)
    description = serializers.CharField(max_length = 1000)
    submitted_by = UserSerializer()
    assigned_to = UserSerializer()
    resolution_status = serializers.CharField(max_length = 50)
    date_created = serializers.DateField()
    date_modified = serializers.DateField()
    author =  UserSerializer()

class QueryCommentSerializer(serializers.Serializer):
    query = QuerySerializer()
    comment = serializers.CharField()
    date_created = serializers.DateField()
    date_modified = serializers.DateField()
    author =  UserSerializer()