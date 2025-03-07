from django.urls import path
from student.views import student_data, student_registration, student_login, student_registration_success, delete_student, view_all_students, update_student

urlpatterns = [
    path('', view_all_students, name='student_home'),
    path('data/', student_data, name='student_data'),
    path('register/', student_registration, name='student_registration'),
    path('register/success/', student_registration_success, name='student_registration_success'),
    path('login/', student_login, name='student_login'),
    path('all/', view_all_students, name='view_all_students'),
    path('delete/<int:stu_id>', delete_student, name='delete_student'),
    path('update/<int:stu_id>', update_student, name='update_student'),
]
