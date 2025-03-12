from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path('', teacher_home, name="home"),
    path('register/', register_teacher, name="register_teacher")
]
