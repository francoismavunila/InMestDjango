from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class UserType(models.Model):
    type_name = models.CharField(max_length=255, unique=True,null = True)
    
    def __str__(self):
        return self.type_name


class IMUser(AbstractUser):
    USER_TYPES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name =  models.CharField(max_length=100, blank=True , null = True)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT')
    
    groups = models.ManyToManyField(Group, related_name = 'imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name = 'imuser_set')
    
    def __str__(self):
        return self.username
    
    # USERNAME_FIELD = 'first_name'
    # REQUIRED_FIELDS = []

    
class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length = 5000)
    year = models.IntegerField()
    start_date = models.DateField(blank = True)
    end_date = models.DateField(blank = True)
    is_active = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(IMUser,on_delete = models.CASCADE)
    


    
    def __str__(self):
        return self.name

class CohorMember(models.Model):
    cohort = models.ForeignKey(Cohort,on_delete = models.CASCADE)
    member = models.ForeignKey(IMUser,on_delete = models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(IMUser,on_delete = models.CASCADE, related_name = "authored_by")
    
    def __str__(self):
        return f"{self.member.first_name} in {self.cohort.name}"