from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from student.models import Profile
from student.myforms import Registration, LogIn
import copy

# Create your views here.
def student_data(request):
    students = Profile.objects.all()
    return render(request, 'student/profile.html', {'students': students})

# Student Registration
def student_registration(request):
    if request.method == 'POST':
        data = Registration(request.POST)
        if data.is_valid():
            last_record = Profile.objects.all().order_by('roll_no').last()
            last_roll_no = 0
            if (last_record != None) and (last_record != 0):
                last_roll_no = last_record.roll_no
            print(last_roll_no)
            my_cleaned_data = copy.deepcopy(data.cleaned_data)
            my_cleaned_data.update({'roll_no': (last_roll_no + 1)})
            print(my_cleaned_data)
            stu = Profile(**my_cleaned_data)
            stu.save()
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

    if req.method == 'POST':
        obj = LogIn(req.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return HttpResponseRedirect('')
        else:
            print('Invalid data!')
    
    else:
        obj = LogIn(auto_id='iska_id_%s')
    return render(req, 'student/login.html', {'form_obj': obj})

def view_all_students(req):
    all_students = Profile.objects.all()
    context = {
        'profiles': all_students
    }
    return render(req, 'student/all_students.html', context)

def update_student(req, stu_id):
    if req.method == 'GET':
        print('Its GET method')
        stu = Profile.objects.get(id=stu_id)
        existing_data = {
            'name': stu.name,
            'email': stu.email,
            'password': stu.password,
            'city': stu.city,
            'stu_class': stu.stu_class
        }
        existing_stu = Registration(data=existing_data)
        print(existing_data)

        return render(req, 'student/update_student.html', {'form_obj': existing_stu})
    elif req.method == 'POST':
        print('Its POST method')
        data = Registration(req.POST)
        if data.is_valid():
            print(data.cleaned_data)
            updated_stu = Profile(id=stu_id ,**data.cleaned_data)
            updated_stu.save()
            return HttpResponseRedirect('/student/all')
        else:
            print('Invalid data!')

    return HttpResponse('Updated')

def delete_student(req, stu_id):
    stu = Profile(id=stu_id)
    deleted_data = stu.delete()
    print(deleted_data)
    return HttpResponseRedirect('/student/all')
