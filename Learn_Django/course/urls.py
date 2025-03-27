from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('addcourse/', add_course, name='add_course'),
    path('getcourses/<int:p_stu_class>', get_courses, name='get_courses'),

    # API's
    path('api/getcourses/<int:p_stu_class>', API_Get_Courses.as_view(), name='api_get_courses'),
    path('api/getcourses/', API_Course_List_using_generic_views.as_view(), name='api_get_all_courses'),
    path('api/addcourse/', api_add_course, name='api_add_course'),
    path('api/deletecourse/<course_id>', api_delete_course, name='api_delete_course'),

    # Course object operations using course_id
    path('api/course/<pk>/get', API_Course_using_generic_views.as_view(), name='get_course_object'),
    path('api/course/<pk>/update', API_Course_using_generic_views.as_view(), name='update_course_object'),
    path('api/course/<pk>/delete', API_Course_using_generic_views.as_view(), name='delete_course_object'),
]

urlpatterns = format_suffix_patterns(urlpatterns)