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
from rest_framework.views import APIView
from django import http
from rest_framework import mixins
from rest_framework import generics

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
@api_view(['GET'])
def api_get_all_courses(req, format=None):
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
@api_view(['GET'])
def api_get_courses(req, p_stu_class, format=None):
    try:
        courses = stu_class_courses(p_stu_class)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(f'Error occurs as: {e}')
        return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@csrf_exempt
def api_add_course(req, format=None):
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
def api_delete_course(req, course_id, format=None):
    c = None
    try:
        c = Course.objects.get(course_id=course_id)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        if not c:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# Class based views
class API_Get_All_Courses(APIView):
    def get(self, req, format=None):
        """
        API for getting all courses. 
        Returns a JSON response
        """
        if req.method == 'GET':
            serializer = CourseSerializer(Course.objects.all(), many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid HTTP method call!'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
class API_Get_Courses(APIView):

    def get(self, req, p_stu_class, format=None):
        try:
            courses = stu_class_courses(p_stu_class)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f'Error occurs as: {e}')
            return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Course object instance class    
class API_Course(APIView):

    def get_course_object(self, pk):
        try:
            instance = Course.objects.get(course_id = pk)
            return instance
        except:
            raise http.Http404

    def get(self, req, p_stu_class, format=None):
        try:
            courses = stu_class_courses(p_stu_class)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f'Error occurs as: {e}')
            return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def put(self, req, p_stu_class, format=None):
        instance = self.get_course_object(p_stu_class)
        serializer = CourseSerializer(instance, data=req.data)

        if serializer.is_valid():
            print('Ha ye valid he!')
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, p_stu_class, format=None):
        try:
            instance = self.get_course_object(p_stu_class)
            instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Implementing class based viewsusing mixins


class API_Course_using_mixins(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)
        
    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)
        
    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)


# Get course list using ***Generic Views***
class API_Course_List_using_generic_views(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class API_Course_using_generic_views(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer