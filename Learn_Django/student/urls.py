from django.urls import path, register_converter
from student.views import *

urlpatterns = [
    path('', student_home, name='student_home'),
    path('data/', student_data, name='student_data'),
    path('register/', student_registration_page, name='student_registration_page'),
    path('register/success/', student_registration_success, name='student_registration_success'),
    path('login/', student_login, name='student_login'),
    path('all/', view_all_students, name='view_all_students'),
    # path('delete/<int:stu_id>', delete_student, name='delete_student'),
    # path('update/<int:stu_id>', update_student, name='update_student'),
    path('jsonfile/', add_stu_from_json, name='add_stu_from_json'),
    path('getstudents/<int:p_stu_class>', api_get_students, name='api_get_students'),
    path('getcourses/<int:stu_class>', fetchCourses, name='fetchCourses'),


    # DRF APIs
    path('create/', API_Student.as_view(), name='create_student'),
    path('<str:student_id>/retrive/', API_Student.as_view(), name='retrive_student'),
    path('<str:student_id>/update/', API_Student.as_view(), name='update_student'),
    path('<str:student_id>/delete/', API_Student.as_view(), name='delete_student'),
]
