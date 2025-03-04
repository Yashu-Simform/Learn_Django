from django.urls import path
from student.views import student_data

urlpatterns = [
    path('data/', student_data, name='student_data')
]
