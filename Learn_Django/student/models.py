from django.db import models

# Create your models here.

class StudentProfile(models.Model):
    student_id = models.CharField(verbose_name='student_id', max_length=100, null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255, default='example@gmail.com', unique=True)
    password = models.CharField(max_length=255, verbose_name='password', null=False, blank=False, default='iron@man-power+')
    city = models.CharField(max_length=70, default='junagadh')
    student_class = models.IntegerField(default=1, choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])

    def __str__(self):
        return self.name
    
    def toJSON(self):
        return {'student_id': self.student_id,
                'name': self.name, 
               'email': self.email,
               'password': self.password,
               'city': self.city,
               'student_class': self.student_class}
    

class Result(models.Model):
    student_id = models.IntegerField(default = 0, unique=True)
    student_class = models.IntegerField(default=1, choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])
    marks = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.student_id)