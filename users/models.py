from django.db import models

# Create your models here.
class UserType(models.Model):
    type_name = models.CharField(max_length=255, unique=True,null = True)
    
    def __str__(self):
        return self.type_name


class IMUser(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name =  models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
    
class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length = 500)
    year = models.IntegerField()
    start_date = models.DateField(blank = True)
    end_date = models.DateField(blank = True)
    is_active = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(IMUser,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name