from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import requests
import json
from .myforms import TeacherRegistration
from .db_operations import add_teacher_db

# Create your views here.
# def teacher_home(req):
#     return render(req, 'teacher/teacher_home.html')


def teacher_home(req):
    base_url = 'http://127.0.0.1:8000/'
    l_url = f'{base_url}course/getcourses/1'
    stu_url = f'{base_url}student/getstudents/5'
    response = requests.get(l_url)
    courses = response.text

    get_stus = requests.get(stu_url)
    print(str(get_stus.text))
    json_data = json.loads(str(get_stus.text))
    students = [stu for stu in json_data.values()]
    print(students)
    return render(req, 'teacher/teacher_home.html', {'courses': courses, 'students': students})

def register_teacher(req):
    if req.method == 'POST':
        data = TeacherRegistration(req.POST)

        if data.is_valid():
            print(data.cleaned_data)
            try:
                add_teacher_db(data.cleaned_data)
                return HttpResponse('<h1>Registration Successfully!</h1>')
            except Exception as e:
                print(f'There occur some error: {e}')
    context = {'form_obj': TeacherRegistration()}
    return render(req, 'teacher/teacher_registration.html', context)