from django.urls import path, include, reverse
from core.middlewares.teacher import AuthCheck
from .views import *
from .app_viewset import *

urlpatterns = [
    path('', teacher_home, name="teacher_home"),
    # path('register/', register_teacher, name="register_teacher"),
    path('loginPage/', teacher_loginPage, name="login_teacher"),
    path('logout/', logout_teacher, name="logout_teacher"),
    # path('delete/<tid>', delete_teacher, name="delete_teacher"),
    path('fetchstudents/<stu_class>/', get_students_view, name="fetchstudents"),
    path('fetchcourses/<stu_class>/', get_courses_view, name="fetchcourses"),

    # DRF - API's
    path('create/', API_Teacher.as_view(), name="create_teacher"),
    path('retrive/<teacher_id>/', API_Teacher.as_view(), name="retrive_teacher"),
    path('update/<teacher_id>/', API_Teacher.as_view(), name="update_teacher"),
    path('delete/<teacher_id>/', API_Teacher.as_view(), name="delete_teacher"),
    path('list/', API_Teacher_List.as_view(), name="retrive_teacher_list"),
    path('login/', API_Teacher_Login.as_view(), name="teacher_login"),
    path('get_or_create/', API_Teacher_List_and_Create.as_view()),
    path('teacherlist-using-viewsets/', teacher_list_view),
    path('teacherdetail-using-viewsets/<teacher_id>', teacher_detail_view, name='teacher-detail'),
]
