from .models import StudentProfile


# Save a single stu record to db
def add_stu_to_db(data):
    last_record = StudentProfile.objects.all().order_by('roll_no').last()
    last_roll_no = 0
    if (last_record != None) and (last_record != 0):
        last_roll_no = last_record.roll_no
    print(last_roll_no)
    data.update({'roll_no': (last_roll_no + 1)})
    stu = StudentProfile(**data)
    stu.save()

def get_students(p_stu_class):
    students = list(StudentProfile.objects.filter(stu_class = p_stu_class))
    final_data = {}
    for i, stu in enumerate(students):
        final_data[i] = stu.toJSON()
    return final_data

def delete_stu_db(p_stu_id):
    try:
        stu = StudentProfile(id=p_stu_id)
        deleted_data = stu.delete()
        print(deleted_data)
    except Exception as e:
        raise e
    
def teacher_id_generator():
    new_id = None
    last_id = StudentProfile.objects.all().order_by('teacher_id').last()
    if last_id == None:
        new_id = 'T001'
    else:
        new_id = 'T' + str(int(last_id[1:]) + 1)
    print(new_id)
    return new_id