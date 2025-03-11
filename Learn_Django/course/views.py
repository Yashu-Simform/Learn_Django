from django.shortcuts import render
from .models import Course
from .myforms import AddCourse

# Create your views here.
def add_course(req):
    context = {'form_obj': AddCourse()}
    return render(req, 'course/add_course.html', context)