from django.shortcuts import render
from .models import Course
from .myforms import AddCourse
from django.http import HttpResponse, JsonResponse
from .db_operations import add_course_db, stu_class_courses

#DRF
from .serializers import CourseSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

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
    

#--------------API's in Django

# get courses for specified stu class
# def api_get_courses(req, p_stu_class):
#     try:
#         courses = stu_class_courses(p_stu_class)
#         json_data = {i: c.toJSON() for i, c in enumerate(courses)}
#         return JsonResponse(json_data)
#     except Exception as e:
#         print(f'Error occurs as: {e}')
#         return HttpResponse(f'Error occurs as: {e}')
    
# def api_get_all_courses(req):
#     try:
#         courses = stu_class_courses()
#         json_data = {i: c.toJSON() for i, c in enumerate(courses)}
#         return JsonResponse(json_data)
#     except Exception as e:
#         print(f'Error occurs as: {e}')
#         return HttpResponse(f'Error occurs as: {e}')
    

#-------------- Django REST Framework - API's

# Returns all courses
def api_get_all_courses(req):
    """
    API for getting all courses. 
    Returns a JSON response
    """
    if req.method == 'GET':
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Invalid HTTP method call!'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

# get courses for specified stu class
def api_get_courses(req, p_stu_class):
    try:
        courses = stu_class_courses(p_stu_class)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(f'Error occurs as: {e}')
        return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@csrf_exempt
def api_add_course(req):
    if req.method == 'POST':
        parsed_data = JSONParser().parse(req)
        serializer = CourseSerializer(data=parsed_data)

        if serializer.is_valid():
            print(serializer.validated_data)
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f'An error occured: {e}')
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    return JsonResponse({},status=404)

# Delete course 
@api_view(['DELETE'])
def api_delete_course(req, course_id):
    c = None
    try:
        c = Course.objects.get(course_id=course_id)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        if not c:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)