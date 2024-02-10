from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(max_length = 500, blank=True,null=True)

    course_date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    course_date_modified = models.DateTimeField(auto_now=True, blank=True,null=True)
    
    def  __str__(self):
        return self.course_name


    

    
    
    