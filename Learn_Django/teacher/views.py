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
from .serializers import TeacherBaseSerializer
from core.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions, authentication
# from core import custom_permissions
from core.custom_permissions import StaffEditorPermissionMixin
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from core.custom_authentication_system import CustomTokenAuth

# Create your views here.
# def teacher_home(req):
#     return render(req, 'teacher/teacher_home.html')

def teacher_home(req):
    try:
        user, token = CustomTokenAuth().auth_using_cookies(req)
    except Exception as e:
        try:
            user, token = TokenAuthentication().authenticate(req)
        except Exception as e:
            print('Error : {e}')
            return HttpResponseRedirect(reverse('login_teacher'))
        print('Error : {e}')
        return HttpResponseRedirect(reverse('login_teacher'))
        
    print((req.headers))
    # if 'loggedin' in req.session and req.session['loggedin'] == True:
    #     print('Ha bhai to achuka he pehle!')
    # else: 
    #     print('Redirect kar raha hu!')
    #     return HttpResponseRedirect(reverse('login'))
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
    students = []
    courses = []
    context = {'courses': courses, 'students': students}
    return render(req, 'teacher/teacher_home.html', context)

# class teacher_home(APIView):
#     def post(self, req):
#         base_url = 'http://127.0.0.1:8000/'
#         l_url = f'{base_url}course/api/getcourses/1'
#         stu_url = f'{base_url}student/getstudents/5'
#         response = requests.get(l_url)
#         json_data = json.loads(str(response.text))
#         print(json_data)
#         courses = [c for c in json_data]
#         print(courses)

#         get_stus = requests.get(stu_url)
#         print(str(get_stus.text))
#         json_data = json.loads(str(get_stus.text))
#         students = [stu for stu in json_data.values()]
#         print(students)
#         students = []
#         courses = []
#         context = {'courses': courses, 'students': students}
#         return render(req, 'teacher/teacher_home.html', context)


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


def teacher_loginPage(req):
    if req.method == 'GET':
        return render(req, 'teacher/login.html', {'form_obj': TeacherLogin()})


def logout_teacher(req):
    # if not req.session['token']:
    #     print('Sale logout to he!')
    
    try:
        # del req.session['loggedin']
        req.session.flush()
        print(req.COOKIES)
        req.COOKIES.pop('token')
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
    context = {'students': students}
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
    context = {'students': courses}
    return render(req, 'teacher/teacher_home.html', context)


# ------------------DRF - API's

# Teacher Model Instance
class API_Teacher(mixins.UpdateModelMixin ,mixins.DestroyModelMixin ,mixins.RetrieveModelMixin ,mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id'

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
    serializer_class = TeacherBaseSerializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)
    

class API_Teacher_Login(APIView):

    def post(self, req, format=None):
        if 'token' in req.COOKIES:
            return HttpResponseRedirect(reverse('teacher_home'))

        serializer = UserSerializer(data=req.data)

        if not serializer.is_valid():
            return Response({
                "status": "False",
                "data": serializer.errors
            })
        
        user_email = serializer.data['email']
        user_password = serializer.data['password']

        user_obj = authenticate(username=user_email,password=user_password)

        if user_obj:
            token, _ = Token.objects.get_or_create(user=user_obj)
            print(token)

            return Response({
                "status": True,
                "data" : {"token": str(token) }
            },
            content_type='json'
            )

        return Response({
            "status": True,
            "data": "Invalid Credentials!"
        })
    
class API_Teacher_Logout(APIView):
    def get(self, req, *args, **kwargs):
        try:
            pass
        except:
            pass
    pass

# Object retrive API
class API_Teacher_Retrive(generics.RetrieveAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id' #primary field name used to get the object 

    # The generic RetriveAPIView class has a default method for 'GET' method so by just inheriting this class you are able to retrive data.

# Object create API
class API_Teacher_Create(generics.CreateAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id' #primary field name used to get the object 

# Object Update API
class API_Teacher_Update(generics.UpdateAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id' #primary field name used to get the object 

# Object delete API
class API_Teacher_Delete(generics.DestroyAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    lookup_field = 'teacher_id' #primary field name used to get the object 

# List of Object API
class API_Teacher_List(generics.ListAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer

# List and Create API for Object
class API_Teacher_List_and_Create(StaffEditorPermissionMixin, generics.ListCreateAPIView):

    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

# Signup or Register Teacher
class API_Teacher_SignUp(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherBaseSerializer

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)
