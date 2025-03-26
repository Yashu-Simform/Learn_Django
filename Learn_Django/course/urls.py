from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('addcourse/', add_course, name='add_course'),
    path('getcourses/<int:p_stu_class>', get_courses, name='get_courses'),

    # API's
    path('api/getcourses/<int:p_stu_class>', api_get_courses, name='api_get_courses'),
    path('api/getcourses/', api_get_all_courses, name='api_get_all_courses'),
    path('api/addcourse/', api_add_course, name='api_add_course'),
    path('api/deletecourse/<course_id>', api_delete_course, name='api_delete_course'),
]

urlpatterns = format_suffix_patterns(urlpatterns)