from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.transaction import atomic
from .db_operations import saveUserFun
from django.contrib.auth.hashers import make_password

# Create your models here.
class TeacherProfile(models.Model):
    teacher_id = models.CharField(verbose_name='teacher_id', max_length=100, null=False, unique=True, primary_key=True, blank=True)
    name = models.CharField(verbose_name='name', max_length=255, null=False)
    email = models.EmailField(verbose_name='email', max_length=255, null=False, unique=True)
    mobile_number = models.CharField(verbose_name='mobile_number', max_length=10, null=False, unique=True)
    address = models.TextField(verbose_name='address', max_length=255)
    specialization = models.CharField(verbose_name='specialization', max_length=255, null=False)
    password = models.CharField(max_length=255, verbose_name='password', null=False, blank=False, default='iron@man-power+')

    @atomic
    def save(self, *args, **kwargs):
        if not self.teacher_id:
            self.teacher_id = TeacherProfile.teacher_id_generator()
        try:
            self.password = make_password(self.password)
            saveUserFun({'email': self.email, 'password': self.password})
        except Exception as e:
            raise e
        return super(TeacherProfile,self).save(*args, **kwargs)

    @staticmethod
    def teacher_id_generator():
        new_id = None
        last_id = TeacherProfile.objects.all().order_by('teacher_id').last()
        if last_id == None:
            new_id = 'T001'
        else:
            new_id = 'T' + str(int(last_id.teacher_id[1:]) + 1).rjust(3, '0')
        print(new_id)
        return new_id