from django.urls import path
from .views import add_course, get_courses

urlpatterns = [
    path('addcourse/', add_course, name='add_course'),
    path('getcourses/<int:p_stu_class>', get_courses, name='get_courses'),
]
