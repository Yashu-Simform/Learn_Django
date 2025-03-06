from django.contrib import admin
from student.models import Profile, Result

# Register your models here.

#It's Optional | We can use the below class to mention what to show on admin panel for a particular relation
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'email')

admin.site.register(Profile, ProfileAdmin)

#Another way to register model for our admin dashboard
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('stu_roll_no', 'stu_class')