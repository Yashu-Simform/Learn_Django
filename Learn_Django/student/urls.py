from django.urls import path
from student.views import student_data, student_registration, student_login, student_registration_success

urlpatterns = [
    path('data/', student_data, name='student_data'),
    path('register/', student_registration, name='student_registration'),
    path('register/success/', student_registration_success, name='student_registration_success'),
    path('login/', student_login, name='student_login'),
]
