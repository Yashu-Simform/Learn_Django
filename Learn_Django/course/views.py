from django.shortcuts import render
from .models import Course
from .myforms import AddCourse
from django.http import HttpResponse
from .db_operations import add_course_db, stu_class_courses

# Create your views here.
def add_course(req):
    if req.method == 'POST':
        data = AddCourse(req.POST)

        if data.is_valid():
            print(data.cleaned_data)
            try:
                add_course_db(data.cleaned_data)
                return render(req, 'course/show_courses.html')
            except Exception as e:
                print(f'There occur some error: {e}')
    context = {'form_obj': AddCourse()}
    return render(req, 'course/add_course.html', context)

def get_courses(req, p_stu_class):
    try:
        courses = stu_class_courses(p_stu_class)
        return HttpResponse('Got the result')
    except Exception as e:
        print(f'Error occurs as: {e}')
        return HttpResponse(f'Error occurs as: {e}')