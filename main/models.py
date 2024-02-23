from django.db import models

from users.models import Cohort, IMUser

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(max_length = 500, blank=True,null=True)

    course_date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    course_date_modified = models.DateTimeField(auto_now=True, blank=True,null=True)
    
    def  __str__(self):
        return self.course_name


class ClassSchedule(models.Model):
    title = models.CharField(max_length = 500, blank=True,null=True)
    description = models.TextField(max_length = 1000, blank=True, null = True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default = False)
    repeat_frequency = models.IntegerField(default = 1)
    is_active = models.BooleanField(default = True)
    organizer = models.CharField(max_length = 255)
    cohort = models.ForeignKey(Cohort, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null=True)
    facilitator = models.ForeignKey(IMUser, on_delete = models.CASCADE, null = True)
    venue = models.CharField(max_length = 255)
    date_created = models.DateField(auto_now_add = True, null = True)
    date_modified = models.DateField(auto_now = True, null = True)
    
    def __str__(self):
        return self.title
    
class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete =models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete = models.CASCADE) 
    is_present = models.BooleanField(default = False)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name = "authored_b_y") 

class Query(models.Model):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    DECLINED = 'DECLINED'
    RESOLVED = 'RESOLVED'
    RESOLUTION_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (DECLINED, 'Declined'),
        (RESOLVED, 'Resolved'),
    ]

    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    submitted_by = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name ="query_submitted_by")
    assigned_to = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name ="query_assigned_to")
    resolution_status = models.CharField(max_length = 50, choices = RESOLUTION_STATUS_CHOICES, default=PENDING)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)
    author =  models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name ="query_author")
    
    def __str__(self):
        return self.title
    
class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 1000, null = True, blank=True)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)
    author =  models.ForeignKey(IMUser, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"query : {self.query.title}  comment {self.comment}"