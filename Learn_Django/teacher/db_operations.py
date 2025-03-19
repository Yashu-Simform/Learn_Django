from .models import TeacherProfile
from django.contrib.auth.hashers import make_password

def saveUser(func):
    from django.contrib.auth.models import User
    def wrapper(p_body):
        user = User.objects.create(email=p_body['email'], password=make_password(p_body['password']))

        user.save()
        func(p_body)

    return wrapper

@saveUser
def add_teacher_db(data = None):
    if data:
        try:
            l_teacher_id = teacher_id_generator()
            data.update({'teacher_id': l_teacher_id})
            new_teacher = TeacherProfile(**data)
            new_teacher.save()
        except Exception as e:
            raise e
    else:
        print('Not enough data!')

def teacher_id_generator():
    new_id = None
    last_id = TeacherProfile.objects.all().order_by('teacher_id').last()
    if last_id == None:
        new_id = 'T001'
    else:
        new_id = 'T' + str(int(last_id[1:]) + 1)
    print(new_id)
    return new_id

# Delete a teacher
def delete_teacher_db(tid):
    try:
        teacher = TeacherProfile.objects.get(teacher_id = tid)
        deleted_data = teacher.delete()
        print('Deleted data: {deleted_data}')
    except Exception as e:
        if not TeacherProfile.objects.filter(teacher_id = tid):
            raise Exception('Teacher with specified id does not exists in db.')
        else:
            raise Exception(f'Error occur while deleting teacher: {e}')