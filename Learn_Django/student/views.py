from django.shortcuts import render
from student.models import Profile

# Create your views here.
def student_data(request):
    students = Profile.objects.all()
    return render(request, 'student/profile.html', {'students': students})