from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from student.models import Profile
from student.myforms import Registration, LogIn, RegistrationFile
import json
from django.contrib import messages

# Create your views here.
def student_data(request):
    students = Profile.objects.all()
    return render(request, 'student/profile.html', {'students': students})

# Student Registration
def student_registration(request):
    if request.method == 'POST':
        data = Registration(request.POST)
        if data.is_valid():
            try:
                messages.info(request, f"Student with data : \n{data.cleaned_data} \nis being registered...")
                add_stu_to_db(data.cleaned_data)
                messages.success(request, "Student Registered Successfully!")
            except Exception as e:
                messages.add_message(request, messages.ERROR, f"There is an error {e}")
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


#View All students
def view_all_students(req):
    all_students = Profile.objects.all()
    # messages.success(req, "Got the students data from db.")

    context = {
        'profiles': all_students,
        'messages': messages.get_messages(req)
    }

    messages.add_message(req, messages.SUCCESS, "Got the students data from db.")
    # messages.add_message(req, messages.ERROR, "Got some error while fetching student data.")
    return render(req, 'student/all_students.html', context)


#Update student record
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
            try:
                updated_stu = Profile(id=stu_id ,**data.cleaned_data)
                updated_stu.save()
                messages.success(req, f"Student with name: {data.cleaned_data.get('name')} is added to db.")
            except Exception as e:
                messages.error(req, f"Got an error for student with email: {data.cleaned_data.get('email')} \nerror: {e}")
                pass
            return HttpResponseRedirect('/student/all')
        else:
            print('Invalid data!')

    return HttpResponse('Updated')


#Delete a student record
def delete_student(req, stu_id):
    try:
        stu = Profile(id=stu_id)
        deleted_data = stu.delete()
        print(deleted_data)
        messages.success(req, "Student deleted successfully!")
    except Exception as e:
        messages.error(req, f"Got some error: {e}")
    return HttpResponseRedirect('/student/all') 

# Add students from JSON file
def add_stu_from_json(req):
    if req.method == 'POST':
        data = RegistrationFile(req.POST, req.FILES)
        if data.is_valid():
            uploaded_file = data.cleaned_data['data_file']
            if uploaded_file:
                print(uploaded_file.name)

                students_data = json.load(uploaded_file)
                print(students_data)

                for stu_data in students_data:
                    try:
                        add_stu_to_db(stu_data)
                        messages.success(req, f"Student with name: {stu_data.get('name')} is added to db.")
                    except Exception as e:
                        messages.error(req, f"Got an error for student with email: {stu_data.get('email')} \nerror: {e}")

        else:
            print('Invalid Data!')
    # print('Students data from file saved to db!')
    else:
        data = RegistrationFile()

    return render(req, 'student/data_file_upload.html', {'form_obj': data})

# Save a single stu record to db
def add_stu_to_db(data):
    last_record = Profile.objects.all().order_by('roll_no').last()
    last_roll_no = 0
    if (last_record != None) and (last_record != 0):
        last_roll_no = last_record.roll_no
    print(last_roll_no)
    data.update({'roll_no': (last_roll_no + 1)})
    stu = Profile(**data)
    stu.save()