from .models import StudentProfile
from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic

def saveUser(func):
    from django.contrib.auth.models import User
    def wrapper(p_body):
        data = {
            'email': p_body['email'],
            'username': p_body['email'],
            'password': make_password(p_body['password']),
            'last_name': 'none',
            'first_name': 'none',
        }
        user = User.objects.create(**data)

        user.save()
        func(p_body)

    return wrapper

# Save a single stu record to db
@atomic
@saveUser
def add_stu_to_db(data):
    if data:
        try:
            l_student_id = student_id_generator()
            data.update({'student_id': l_student_id})
            data['password'] = make_password(data['password'])
            new_student = StudentProfile(**data)
            new_student.save()
        except Exception as e:
            raise e
    else:
        print('Not enough data!')

def get_students(p_stu_class):
    students = list(StudentProfile.objects.filter(student_class = p_stu_class))
    final_data = {}
    for i, stu in enumerate(students):
        final_data[i] = stu.toJSON()
    return final_data

def delete_stu_db(p_stu_id):
    try:
        stu = StudentProfile(student_id=p_stu_id)
        deleted_data = stu.delete()
        print(deleted_data)
    except Exception as e:
        raise e
    
def student_id_generator():
    new_id = None
    last_id = StudentProfile.objects.all().order_by('student_id').last()
    if last_id == None:
        new_id = 'S001'
    else:
        new_id = 'S' + str(int(last_id.student_id[1:]) + 1)
    print(new_id)
    return new_id