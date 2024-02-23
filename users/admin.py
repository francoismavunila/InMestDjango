from django.contrib import admin

from users.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","is_active","user_type")
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','is_active','year','start_date','end_date','author')

class CohortMember(admin.ModelAdmin):
    list_display = ('id','cohort','member')
# Register your models here.
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(IMUser, UserAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohorMember, CohortMember)
