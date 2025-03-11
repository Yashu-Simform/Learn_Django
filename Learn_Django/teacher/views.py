from django.shortcuts import render

# Create your views here.
def teacher_home(req):
    return render(req, 'teacher/teacher_home.html')