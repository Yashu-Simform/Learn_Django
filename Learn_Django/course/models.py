from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255,verbose_name='course_name')
    stu_class = models.IntegerField(verbose_name='stu_class',choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])