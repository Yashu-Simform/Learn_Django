from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'teacher/base.html')