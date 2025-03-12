from django.shortcuts import render
from .models import Course
from .myforms import AddCourse
from django.http import HttpResponse, JsonResponse
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
        return render(req, 'course/show_courses.html', {'courses': courses})
    except Exception as e:
        print(f'Error occurs as: {e}')
        return HttpResponse(f'Error occurs as: {e}')
    

# API's 

# get courses for specified stu class
def api_get_courses(req, p_stu_class):
    try:
        courses = stu_class_courses(p_stu_class)
        json_data = {i: c.toJSON() for i, c in enumerate(courses)}
        return JsonResponse(json_data)
    except Exception as e:
        print(f'Error occurs as: {e}')
        return HttpResponse(f'Error occurs as: {e}')
    
def api_get_all_courses(req):
    try:
        courses = stu_class_courses()
        json_data = {i: c.toJSON() for i, c in enumerate(courses)}
        return JsonResponse(json_data)
    except Exception as e:
        print(f'Error occurs as: {e}')
        return HttpResponse(f'Error occurs as: {e}')