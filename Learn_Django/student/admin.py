from django.contrib import admin
from student.models import StudentProfile, Result

# Register your models here.

#It's Optional | We can use the below class to mention what to show on admin panel for a particular relation
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(StudentProfile, ProfileAdmin)

#Another way to register model for our admin dashboard
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_class')