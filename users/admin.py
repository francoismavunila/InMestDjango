from django.contrib import admin

from users.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","is_active","user_type")
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
# Register your models here.
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(IMUser, UserAdmin)
admin.site.register(Cohort)
