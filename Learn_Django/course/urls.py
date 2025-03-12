from django.urls import path
from .views import *

urlpatterns = [
    path('addcourse/', add_course, name='add_course'),
    path('getcourses/<int:p_stu_class>', get_courses, name='get_courses'),
    path('api/getcourses/<int:p_stu_class>', api_get_courses, name='api_get_courses'),
    path('api/getcourses/', api_get_all_courses, name='api_get_all_courses'),
]
