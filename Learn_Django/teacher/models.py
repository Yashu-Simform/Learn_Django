from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class TeacherProfile(models.Model):
    teacher_id = models.CharField(verbose_name='teacher_id', max_length=100, null=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name='name', max_length=255, null=False)
    email = models.EmailField(verbose_name='email', max_length=255, null=False, unique=True)
    mobile_number = models.CharField(verbose_name='mobile_number', max_length=10, null=False, unique=True)
    address = models.TextField(verbose_name='address', max_length=255)
    specialization = models.CharField(verbose_name='specialization', max_length=255, null=False)
    password = models.CharField(max_length=50, verbose_name='password', null=False, blank=False, default='iron@man-power+')