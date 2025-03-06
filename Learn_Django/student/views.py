from django.shortcuts import render, HttpResponseRedirect
from student.models import Profile
from student.myforms import Registration, LogIn

# Create your views here.
def student_data(request):
    students = Profile.objects.all()
    return render(request, 'student/profile.html', {'students': students})

# Student Registration
def student_registration(request):
    if request.method == 'POST':
        data = Registration(request.POST)
        if data.is_valid():
            print(data.cleaned_data)
            return HttpResponseRedirect('/student/register/success')
        else:
            print('Invalid data!')
    else:
        print('Request method is not POST')
        data = Registration()
    return render(request, 'student/registration.html', {'form_obj': data})


def student_registration_success(req):
    return render(req, 'student/register_success.html')

# Student Login
def student_login(req):
    obj = LogIn(auto_id='iska_id_%s')
    return render(req, 'student/login.html', {'form_obj': obj})