from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path('', teacher_home, name="teacher_home"),
    path('register/', register_teacher, name="register_teacher"),
    path('login/', login_teacher, name="login_teacher"),
    path('logout/', logout_teacher, name="logout_teacher"),
    path('delete/<tid>', delete_teacher, name="delete_teacher"),
]
