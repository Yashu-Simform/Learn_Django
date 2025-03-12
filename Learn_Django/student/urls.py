from django.urls import path, register_converter
from student.views import *

urlpatterns = [
    path('', view_all_students, name='student_home'),
    path('data/', student_data, name='student_data'),
    path('register/', student_registration, name='student_registration'),
    path('register/success/', student_registration_success, name='student_registration_success'),
    path('login/', student_login, name='student_login'),
    path('all/', view_all_students, name='view_all_students'),
    path('delete/<int:stu_id>', delete_student, name='delete_student'),
    path('update/<int:stu_id>', update_student, name='update_student'),
    path('jsonfile/', add_stu_from_json, name='add_stu_from_json'),
    path('getstudents/<int:p_stu_class>', api_get_students, name='api_get_students'),
]
