from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.shortcuts import render
from django.urls import reverse
import requests
import json
from .myforms import TeacherRegistration, TeacherLogin
from .db_operations import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import TeacherProfile
from django.contrib import messages

# DRF
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .serializers import TeacherSerializer
from core.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
# def teacher_home(req):
#     return render(req, 'teacher/teacher_home.html')

def teacher_home(req):
    if 'loggedin' in req.session and req.session['loggedin'] == True:
        print('Ha bhai to achuka he pehle!')
    else:
        print('Redirect kar raha hu!')
        return HttpResponseRedirect(reverse('login'))
    base_url = 'http://127.0.0.1:8000/'
    l_url = f'{base_url}course/api/getcourses/1'
    stu_url = f'{base_url}student/getstudents/5'
    response = requests.get(l_url)
    json_data = json.loads(str(response.text))
    print(json_data)
    courses = [c for c in json_data]
    print(courses)

    get_stus = requests.get(stu_url)
    print(str(get_stus.text))
    json_data = json.loads(str(get_stus.text))
    students = [stu for stu in json_data.values()]
    print(students)
    students = get_students_view()  
    courses = get_courses_view()
    context = {'courses': courses, 'students': students, 'loggedin': req.session['loggedin']}
    return render(req, 'teacher/teacher_home.html', context)


# def register_teacher(req):
#     if req.method == 'POST':
#         data = TeacherRegistration(req.POST)

#         if data.is_valid():
#             print(data.cleaned_data)
#             try:
#                 add_teacher_db(data.cleaned_data)
#                 return HttpResponse('<h1>Registration Successfully!</h1>')
#             except Exception as e:
#                 print(f'There occur some error: {e}')
#     context = {'form_obj': TeacherRegistration()}
#     return render(req, 'teacher/teacher_registration.html', context)


def login_teacher(req):
    if req.method == 'POST':
        #Authenticate user from db
        print(f'Login req body: {req.POST}')
        
        response = TeacherLogin(req.POST)
        if response.is_valid():
            print(response.cleaned_data['email'])
            user = list(User.objects.filter(email=response.cleaned_data['email']))
            print(user)
            if len(user) > 0:
                login(req, user[0])
                req.session['loggedin'] = True
                return HttpResponseRedirect(reverse('teacher_home'))
            else:
                print('No such user exists!')
                messages.add_message(req, messages.ERROR, 'No such user exists!')
        pass
    else:
        response = TeacherLogin()
    
    return render(req, 'teacher/login.html', {'form_obj': response})


def logout_teacher(req):
    if not req.session['loggedin']:
        print('Sale logout to he!')
    
    try:
        # del req.session['loggedin']
        req.session.flush()
        return HttpResponseRedirect(reverse('project_home'))
    except Exception as e:
        print(f'Error while logging out: {e}')

    return HttpResponseRedirect(reverse('teacher_home')) 


# def delete_teacher(req, tid):
#     try:
#         delete_teacher_db(tid)
#         return HttpResponse('Teacher Deleted Successfully!')
#     except Exception as e:
#         print(e)
#         return HttpResponse(f'{e}')

def get_students_view(req, stu_class):
    base_url = 'http://127.0.0.1:8000/'
    stu_url = f'{base_url}student/getstudents/{stu_class}'
    get_stus = requests.get(stu_url)
    print(str(get_stus.text))
    json_data = json.loads(str(get_stus.text))
    students = [stu for stu in json_data.values()]
    print(students)
    # return students
    context = {'students': students, 'loggedin': req.session['loggedin']}
    return render(req, 'teacher/teacher_home.html', context)


def get_courses_view(req, stu_class=1):
    base_url = 'http://127.0.0.1:8000/'
    courses_url = f'{base_url}course/api/getcourses/{stu_class}'
    response = requests.get(courses_url)
    json_data = json.loads(str(response.text))
    print(json_data)
    courses = [c for c in json_data]
    print(courses)
    # return courses
    context = {'students': courses, 'loggedin': req.session['loggedin']}
    return render(req, 'teacher/teacher_home.html', context)


# ------------------DRF - API's

# Teacher Model Instance
class API_Teacher(mixins.UpdateModelMixin ,mixins.DestroyModelMixin ,mixins.RetrieveModelMixin ,mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)
    
    def get(self, req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)
    
    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)

    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)
    

class API_Teacher_List(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)
    

class API_Teacher_Login(APIView):

    def post(self, req, format=None):
        user = get_object_or_404(User, email=req.data['email'])

        serializer = UserSerializer(User.objects.all())
        # return Response()
        return Response({})


class API_Teacher_SignUp(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)