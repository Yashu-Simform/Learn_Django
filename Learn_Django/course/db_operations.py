from .models import Course

def add_course_db(p_data):
    acourse = Course(**p_data)
    acourse.save()

def stu_class_courses(p_stu_class = None):
    result = []
    if p_stu_class:
        result = list(Course.objects.filter(stu_class=p_stu_class))
    else:
        result = list(Course.objects.all())
    return result